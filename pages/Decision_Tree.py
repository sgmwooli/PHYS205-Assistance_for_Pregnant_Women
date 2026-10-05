import streamlit as st
import pandas as pd
from datetime import datetime
from sklearn import tree

st.set_page_config(page_title="Decision Tree")

##################################################################################
file_path = "/Users/maxwooliscroft/Desktop/NEW_Website_-_PHYS205_-_Long_Project" # <- EDIT
##################################################################################

class Patient:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.weeks_pregnant = 0
        self.trimester = 0

    def get_age(self):
        today = datetime.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    def determine_trimester(self):
        if self.weeks_pregnant < 13:
            self.trimester = 1
        elif 13 <= self.weeks_pregnant < 27:
            self.trimester = 2
        else:
            self.trimester = 3
        return self.trimester

# Streamlit UI
st.title("Pregnancy Symptom Checker")

name_input = st.text_input("Enter your name")
dob_input = st.date_input("Enter your date of birth", min_value="1900-01-01", max_value="today")
weeks_pregnant = st.number_input("How many weeks pregnant are you?", min_value=0, max_value=42)

if name_input and dob_input and weeks_pregnant:
    patient1 = Patient(name_input, dob_input)
    patient1.weeks_pregnant = weeks_pregnant
    trimester = patient1.determine_trimester()
    
    st.markdown(f"### Welcome {patient1.name}!")
    st.write(f"Your age is: {patient1.get_age()} years")
    st.write(f"You are in the **{['first', 'second', 'third'][trimester - 1]}** trimester.")
    
    # Load dataset and symptoms
    if trimester == 1:
        df = pd.read_csv(f"{file_path}/pages/TestingTrimester1.csv")
        symptom_list = ['vaginal bleeding', 'more frequent urination', 'shoulder pain', 'fatigue', 'vomiting', 'abdominal pain',
                        'decreased pregnancy symptoms', 'dizziness', 'thrush', 'yellowing of eyes or skin', 'weight loss',
                        'constipation', 'swelling', 'blood in urine']
        diagnosis_mapping = {'ectopic pregnancy': 1, 'miscarriage': 2, 'infection': 3, 'hyperemesis gravidarum': 4, 'high blood pressure': 5, 'N/A': 0}
    elif trimester == 2:
        df = pd.read_csv(f"{file_path}/pages/TestingTrimester2.csv")
        symptom_list = ['fever', 'joint pain', 'fatigue', 'vaginal bleeding', 'back ache', 'abdominal pain',
                        'decreased pregnancy symptoms', 'dizziness', 'vomiting', 'thrush', 'yellowing of eyes or skin',
                        'more frequent urination', 'hemeroids', 'increased thirst', 'dry mouth', 'vision problems']
        diagnosis_mapping = {'auto-immune disease': 1, 'miscarriage': 2, 'infection': 3, 'gestational diabetes': 4, 'incompetent cervix': 5, 'N/A': 0}
    else:
        df = pd.read_csv(f"{file_path}/pages/TestingTrimester3.csv")
        symptom_list = ['vomiting', 'thrush', 'yellowing of eyes or skin', 'fatigue', 'more frequent urination',
                        'decreased pregnancy symptoms', 'vaginal bleeding', 'shoulder pain', 'dizziness', 'abdominal pain',
                        'severe headaches', 'vision problems', 'contractions', 'back pain']
        diagnosis_mapping = {'infection': 1, 'miscarriage': 2, 'pre-eclampsia': 3, 'placental abruption': 4, 'N/A': 0}

    # Prepare training data
    reverse_diagnosis_mapping = {v: k for k, v in diagnosis_mapping.items()}
    df['Diagnosis'] = df['Diagnosis'].map(diagnosis_mapping)
    df = df.dropna(subset=['Diagnosis'])
    X_train = df[symptom_list].values
    y_train = df[['Diagnosis']].values
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    st.markdown("### Select any symptoms you are experiencing:")
    selected_symptoms = [symptom for symptom in symptom_list if st.checkbox(symptom)]

    if st.button("Submit Symptoms"):
        if not selected_symptoms:
            st.warning("No diagnosis can be made. If concerned, please seek medical advice.")
        else:
            symptom_vector = [1 if symptom in selected_symptoms else 0 for symptom in symptom_list]
            prediction = clf.predict([symptom_vector])[0]
            if prediction == 0:
                st.success("No disease predicted.")
            else:
                predicted_disease = reverse_diagnosis_mapping[prediction]
                st.error(f"The most likely diagnosis is **{predicted_disease}**.\n\nPlease consult a medical professional.")

st.page_link("Homepage.py", label="Home", icon="🏠")