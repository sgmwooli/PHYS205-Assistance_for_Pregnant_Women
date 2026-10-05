import numpy as np
import pandas as pd
import streamlit as st
import openrouteservice
import pandas as pd
import streamlit as st
import urllib.parse
import re
from geopy.geocoders import Nominatim

ORS_API_key = "5b3ce3597851110001cf624850338f1a21864336a544e8222072ba15"

def route(google_maps_link, api_key=ORS_API_key, mode_of_transport='driving-car'):

    ORS_API_key = api_key

    # Get Origin & Destination Coordinates
    def extract_coords_from_url_and_geocode(url, ors_api_key=ORS_API_key):
        import urllib.parse
        import openrouteservice

        parsed = urllib.parse.urlparse(url)
        query = urllib.parse.parse_qs(parsed.query)

        origin_str = query.get('origin', [None])[0]
        destination_str = query.get('destination', [None])[0]

        if origin_str:
            origin_str = urllib.parse.unquote(origin_str)  ###
            origin_lat, origin_lng = map(float, origin_str.split(','))
        else:
            origin_lat = origin_lng = None

        client = openrouteservice.Client(key=ors_api_key)

        # Use ORS geocoding to get a clean destination
        dest_coords = None
        if destination_str:
            destination_str = urllib.parse.unquote(destination_str)  ###
            try:
                geocode_results = client.pelias_search(text=destination_str)
                print(geocode_results['features'][0])
                if geocode_results['features']:
                    coords = geocode_results['features'][0]['geometry']['coordinates']
                    print("Geocoder result preview:", geocode_results['features'][0]['properties']['label'])
                    dest_lng, dest_lat = coords  # ORS returns [lng, lat]
                else:
                    dest_lat = dest_lng = None
            except Exception as e:
                print(f"Geocoding failed for destination: \n{e}")
                dest_lat = dest_lng = None
        else:
            dest_lat = dest_lng = None

        origin, destination = (origin_lng, origin_lat), (dest_lng, dest_lat)
        origin, destination = list(origin), list(destination)

        return origin, destination

    #google_maps_link = "https://www.google.com/maps/dir/?api=1&origin=52.95865772404608%2c-2.180066485093525&destination=Newcastle+Road%2c+Stoke-on-Trent%2c+Staffordshire%2c+ST4+6QG&t=m"  # ST4 -> RS,UHNM
    #google_maps_link = "https://www.google.com/maps/dir/?api=1&origin=53.40091252373974%2c-2.9628093953075187&destination=Prescot+Street%2c+Liverpool%2c+Merseyside%2c+L7+8XP&t=m"  # Melville -> RLUH
    #google_maps_link = "https://www.google.com/maps/dir/?api=1&origin=52.81005506287036%2c-2.082412814007154&destination=Weston+Road%2c+Stafford%2c+Staffordshire%2c+ST16+3SA&t=m"  # S,SFRS -> CH,UHNM
    #google_maps_link = "https://www.google.com/maps/dir/?api=1&origin=53.03634601957967%2c-2.1650748544699177&destination=Newcastle+Road%2c+Stoke-on-Trent%2c+Staffordshire%2c+ST4+6QG&t=m"  # ST1 - RS,UHNM
    #google_maps_link = "https://www.google.com/maps/dir/?api=1&origin=51.48794600884484%2c-0.07424661964059873&destination=Denmark+Hill%2c+London%2c+SE5+9RS&t=m"
    #google_maps_link = st.chat_input("Google Maps URL: ")
    #google_maps_link = st.text_input("Google Maps URL: ")

    origin, destination = extract_coords_from_url_and_geocode(google_maps_link)
    print("Origin:", origin, type(origin))
    print("Destination:", destination, type(destination))

    # 1 - Setup API client
    client = openrouteservice.Client(key=ORS_API_key)  # Get it from openrouteservice.org

    # 2 - Set start and end locations
    coords = [origin, destination]
    #print(coords)

    # 3 - Get route as GeoJSON
    try:
        # Get the route
        route = client.directions(coords, profile=mode_of_transport, format='geojson')
    except openrouteservice.exceptions.ApiError as e:
        # If routing fails, this section allows for debugging
        st.error(f"Routing failed! \n{e}")
        st.stop()

    # 4. Extract coordinates and convert to DataFrame
    raw_coords = route['features'][0]['geometry']['coordinates']
    df = pd.DataFrame(raw_coords, columns=['longitude', 'latitude'])
    df['size'] = [5] * len(df)  # Sizes are all level 5
    df['colour'] = ["#DA291C80"]*len(df)  # Colour is red
    #print(len(df))
    return df

### #google_maps_link = "https://www.google.com/maps/dir/?api=1&origin=52.95865772404608%2c-2.180066485093525&destination=Newcastle+Road%2c+Stoke-on-Trent%2c+Staffordshire%2c+ST4+6QG&t=m"  # ST4 -> RS,UHNM
### google_maps_link = "https://www.google.com/maps/dir/?api=1&origin=53.40091252373974%2c-2.9628093953075187&destination=Prescot+Street%2c+Liverpool%2c+Merseyside%2c+L7+8XP&t=m"  # Melville -> RLUH
### #google_maps_link = "https://www.google.com/maps/dir/?api=1&origin=52.81005506287036%2c-2.082412814007154&destination=Weston+Road%2c+Stafford%2c+Staffordshire%2c+ST16+3SA&t=m"  # S,SFRS -> CH,UHNM
### #google_maps_link = "https://www.google.com/maps/dir/?api=1&origin=53.03634601957967%2c-2.1650748544699177&destination=Newcastle+Road%2c+Stoke-on-Trent%2c+Staffordshire%2c+ST4+6QG&t=m"  # ST1 - RS,UHNM
### #google_maps_link = "https://www.google.com/maps/dir/?api=1&origin=51.48794600884484%2c-0.07424661964059873&destination=Denmark+Hill%2c+London%2c+SE5+9RS&t=m"
### #google_maps_link = st.chat_input("Google Maps URL: ")
### #google_maps_link = st.text_input("Google Maps URL: ")
### df = route(google_maps_link)
### 
### # 5. Streamlit webpage
### st.title("Route Map from A to B")
### 
### # 6. Show DataFrame (optional)
### st.write("Route Data")
### st.dataframe(df)
### 
### # 7. Show on map
### st.map(df, color='colour', size='size', zoom=11)
### 
### print(f"\n\nSuccessfull Execution")
