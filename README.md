# How to view our project:

## Open streamlit web app: "phys205-long-project-2025.streamlit.app"
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://phys205-long-project-2025.streamlit.app/)

## OR, run the web app locally:
   ### 1) Ensure that all necessary libraries are installed via pip:
   	•	time
   	•	random
   	•	IPython.display
   	•	numpy
   	•	pandas
   	•	selenium
   	•	geocoder
   	•	streamlit
   	•	sqlite3
   	•	nltk
   	•	openrouteservice
   	•	ipywidgets
   	•	sklearn
   	•	webdriver_manager
   	•	geopy
   	•	folium
   	•	streamlit_folium

   ### 2) To open our webpage locally, you need to run the terminal command:
	`streamlit run [file_path]/Homepage.py`
then
```bash
brew install --cask google-chrome
pip install -U webdriver-manager
streamlit run /Users/maxwooliscroft/Desktop/COMP_PROJECT_WEBPAGE_3/Website3.py
```

### Troubleshooting:
If you receive this error message:
```
	selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: stale element not found (Session info: chrome=135.0.7049.115); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#stale-element-reference-exception Stacktrace: 0 chromedriver 0x00000001048eaa54 cxxbridge1$str$ptr + 2803960 1 chromedriver 0x00000001048e2cf0 cxxbridge1$str$ptr + 2771860 2 chromedriver 0x000000010442e864 cxxbridge1$string$len + 93028 3 chromedriver 0x000000010443f1d4 cxxbridge1$string$len + 160980 4 chromedriver 0x000000010443e2b8 cxxbridge1$string$len + 157112 5 chromedriver 0x0000000104434d6c cxxbridge1$string$len + 118892 6 chromedriver 0x0000000104434e78 cxxbridge1$string$len + 119160 7 chromedriver 0x0000000104433520 cxxbridge1$string$len + 112672 8 chromedriver 0x0000000104436a4c cxxbridge1$string$len + 126284 9 chromedriver 0x00000001044b7178 cxxbridge1$string$len + 652408 10 chromedriver 0x00000001044b6480 cxxbridge1$string$len + 649088 11 chromedriver 0x00000001044697ec cxxbridge1$string$len + 334572 12 chromedriver 0x00000001048afccc cxxbridge1$str$ptr + 2562928 13 chromedriver 0x00000001048b2f98 cxxbridge1$str$ptr + 2575932 14 chromedriver 0x00000001048902c4 cxxbridge1$str$ptr + 2433384 15 chromedriver 0x00000001048b3810 cxxbridge1$str$ptr + 2578100 16 chromedriver 0x00000001048812f0 cxxbridge1$str$ptr + 2371988 17 chromedriver 0x00000001048d357c cxxbridge1$str$ptr + 2708512 18 chromedriver 0x00000001048d3708 cxxbridge1$str$ptr + 2708908 19 chromedriver 0x00000001048e293c cxxbridge1$str$ptr + 2770912 20 libsystem_pthread.dylib 0x000000019c2eac0c _pthread_start + 136 21 libsystem_pthread.dylib 0x000000019c2e5b80 thread_start + 8
Traceback:
File "/Users/maxwooliscroft/Desktop/Comp_Website/Website2.py", line 49, in <module>
    directions_link, hospital_name, hospital_link, opening_times, address, phone_number = NH.DirectionsFromPostcodeWeb2(PostCode)
                                                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Users/maxwooliscroft/Desktop/Comp_Website/NearestHospital.py", line 145, in DirectionsFromPostcodeWeb2
    google_maps_link = google_maps_link_element.get_attribute("href")
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/selenium/webdriver/remote/webelement.py", line 178, in get_attribute
    attribute_value = self.parent.execute_script(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/selenium/webdriver/remote/webdriver.py", line 414, in execute_script
    return self.execute(command, {"script": script, "args": converted_args})["value"]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/selenium/webdriver/remote/webdriver.py", line 354, in execute
    self.error_handler.check_response(response)
File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/selenium/webdriver/remote/errorhandler.py", line 229, in check_response
    raise exception_class(message, screen, stacktrace)
```
Then execute the following commands in a new terminal window*:
```
brew install --cask google-chrome
pip install -U webdriver-manager
```

\* This has been tested using MacOS, this workaround may not work on Windows/Linux.
