"""Makes a call and returns list of visible sattelites at local"""

from flask import Flask
import requests

BASE_URL= "https://www.n2yo.com/rest/v1/satellite/"
api_key="U9J35D-GT6QWZ-FPTKCN-4KD4" #don't abuse my lack of privacy team

#Test coordinates (Milwaukee)
# lat 43.038902

# lng -87.906471

def vis_sat_ids(lat, lng, alt=0, rad=70):
    """Returns List of Sattelite Norad IDs if Visible from specified location"""
    sats = requests.get(f"{BASE_URL}/above/{str(lat)}/{str(lng)}/{str(alt)}/{str(rad)}/0/&apiKey={api_key}").json()["above"]
    sat_ids = [sat["satid"] for sat in sats]
    return sat_ids
