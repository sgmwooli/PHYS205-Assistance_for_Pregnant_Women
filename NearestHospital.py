from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import geocoder

def CurrentLocation():
    g = geocoder.ip('me')
    latlong = str(g.latlng)
    llstring = str(latlong[1:-1])
    return(llstring)

latlong = CurrentLocation()
#latlong = "53.406404, -2.967531"
#latlong = "52.957984, -2.179879"

def browser(open="Y"):
    if not open=="Y":
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 10)
    else:
        # Open Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        wait = WebDriverWait(driver, 10)
    return driver, wait

def DirectionsFromCurrentLocation():
    driver, wait = browser("N")  # Ensures that the browser opens so that troubleshooting is easier, this will the changed to `browser("N")` in the final script.

    # Go to the website
    driver.get("https://findthatpostcode.uk/")  # Postcode from LatLong

    # Find the text input field
    text_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "q")))

    # Type a search query
    text_field.send_keys(latlong)

    # Press Enter to search
    text_field.send_keys(Keys.RETURN)

    # Wait for results to load

    # Use the XPath
    postcode_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/header/h3/a")))

    # Extract postcode
    nearest_postcode = postcode_element.text

    # Print postcode
    print(f"Nearest postcode to current position ({latlong}) is '{nearest_postcode}'")

    # Replace ' ' in postcode with '%20'
    postcode_NoSpace = nearest_postcode.replace(' ', '%20')
    print(postcode_NoSpace)

    # Go to NHS website
    NHS_WebAddress = f"https://www.nhs.uk/service-search/hospital/results?location={postcode_NoSpace}"
    driver.get(NHS_WebAddress)  # Nearest Hospital from Postcode

    # Find google maps link
    google_maps_link_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "(opens in Google Maps)")))
    google_maps_link = google_maps_link_element.get_attribute("href")

    # Open google maps link
    driver, wait = browser("Y")
    driver.get(google_maps_link)

    # # Close browser
    # input("Press Enter to close...")  # Keeps the window open for you to check
    # driver.quit()
    return

def DirectionsFromPostcode(PostCode):
    driver, wait = browser("N")
    postcode_NoSpace = PostCode.replace(' ', '%20')
    print(postcode_NoSpace)

    # Go to NHS website
    NHS_WebAddress = f"https://www.nhs.uk/service-search/hospital/results?location={postcode_NoSpace}"
    driver.get(NHS_WebAddress)  # Nearest Hospital from Postcode

    # Find google maps link
    google_maps_link_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "(opens in Google Maps)")))
    google_maps_link = google_maps_link_element.get_attribute("href")

    # Open google maps link
    driver, wait = browser("Y")
    driver.get(google_maps_link)
    return

def DirectionsFromPostcodeWeb(PostCode):
    driver, wait = browser("N")
    postcode_NoSpace = PostCode.replace(' ', '%20')
    print(postcode_NoSpace)

    # Go to NHS website
    NHS_WebAddress = f"https://www.nhs.uk/service-search/find-an-accident-and-emergency-service/results/{postcode_NoSpace}"
    driver.get(NHS_WebAddress)  # Nearest Hospital from Postcode

    # Select only open services
    open_services = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "filter_option_0_0")))
    if not open_services.is_selected():
        open_services.click()
    apply = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "apply-filters-button")))
    apply.click()

    # Find google maps link
    google_maps_link_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "(opens in Google Maps)")))
    google_maps_link = google_maps_link_element.get_attribute("href")

    # Open google maps link
    #driver, wait = browser("Y")
    #driver.get(google_maps_link)
    return google_maps_link


def DirectionsFromPostcodeWeb2(PostCode):
    driver, wait = browser("N")
    postcode_caps = PostCode.upper()
    postcode_NoSpace = postcode_caps.replace(' ', '%20')
    print(postcode_NoSpace)

    # Go to NHS website
    NHS_WebAddress = f"https://www.nhs.uk/service-search/find-an-accident-and-emergency-service/results/{postcode_NoSpace}"
    driver.get(NHS_WebAddress)  # Nearest Hospital from Postcode

    # Select only open services
    open_services = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "filter_option_0_0")))
    if not open_services.is_selected():
        open_services.click()
    apply = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "apply-filters-button")))
    apply.click()

    # Find google maps link
    google_maps_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "(opens in Google Maps)"))).get_attribute("href")

    # Find name of Hospital
    hospital = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Hospital")))
    hospital_name = hospital.text.strip()
    hospital_name = hospital_name[31:]
    hospital_link = hospital.get_attribute("href")

    # Find opening times
    opening_times = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "opening_times_list_0_0")))

    # Find address
    address_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "address_0")))
    address_info = address_element.text.strip()
    address = address_info[:7] + ': ' + address_info[35:]
    
    # Find phone number
    phone_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "phone_0")))
    phone_info = phone_element.text.strip()
    phone_number = phone_info[40:]

    # Open google maps link
    #driver, wait = browser("Y")
    #driver.get(google_maps_link)
    return google_maps_link, hospital_name, hospital_link, opening_times, address, phone_number

### directions_link, hospital_name, hospital_link, opening_times, address, phone_number = DirectionsFromPostcodeWeb2("ST4 8ST")
### print(len("navigates to more detail for"))
### print(f"\nYour nearest A&E service is [{hospital_name}]({hospital_link})")
### print(f"\n{address}")
### print(f"Directions can be found [here]({directions_link})")
### print(f"\nThe phone number for this A&E department is {phone_number}")