import streamlit as st
from streamlit_folium import st_folium
import folium
import NearestHospital as NH
import map_test as router

st.set_page_config(page_title="Closest Hospital")

st.title("Find Your Closest Hospital Here")

#st.divider()
PostCode = st.text_input("Enter Current Postcode: ")
st.text("Click 'enter' on the keyboard before clicking the enter button below.")

button1 = st.button('Enter')
if button1 or PostCode[-2:] == '\n':
    directions_link, hospital_name, hospital_link, opening_times, address, phone_number = NH.DirectionsFromPostcodeWeb2(PostCode)
    phone_number_no_space = "".join(phone_number.split())
    st.header("Your Nearest Hospital:")
    st.markdown(f"\nYour nearest A&E service is [{hospital_name}]({hospital_link})  "
                f"\n{address}  "
                f"\n \- (Directions can be found [here]({directions_link}), or see the map below)  "
                f"\nThe phone number for this A&E department is [{phone_number}](tel:{phone_number_no_space})")
    route_df = router.route(directions_link)
    st.map(route_df, color='colour', size='size', zoom=11)

st.page_link("Homepage.py", label="Home", icon="🏠")