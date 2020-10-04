"""Makes a call using sat name and returns the wiki page content"""

from flask import Flask, jsonify
import requests
from models import db, connect_db, Satellite
from dotenv import load_dotenv
import os
from categories import categories
load_dotenv()
# n2yo strings
N2YO_BASE_URL = "https://www.n2yo.com/rest/v1/satellite/"
NEWS_BASE_URL = "https://spaceflightnewsapi.net/api/v1/articles?search="
api_key = os.getenv("n2yo_api_key")

# wiki strings
WIKI_BASE_URL = "https://en.wikipedia.org/w/api.php?action=parse&page="
FORMAT_PARAMETERS_HTML = "&format=json&prop=text&formatversion=2"
FORMAT_PARAMETERS_WIKITEXT = "&format=json&prop=wikitext&formatversion=2"


def call_wikitext(search_term):
    """Returns response in WikiText format. If response is error, returns list of USA Satellites"""

    resp = requests.get(
        f"{WIKI_BASE_URL}{search_term}{FORMAT_PARAMETERS_WIKITEXT}").json()
    if "error" in resp:
        return requests.get(f"{WIKI_BASE_URL}List_of_USA_satellites{FORMAT_PARAMETERS_WIKITEXT}").json()["parse"]["wikitext"]
    else:
        return parse_for_sat(resp['parse']['wikitext'], search_term)


def parse_for_sat(response, search_term):
    sat_count = response.count('atellite')
    if sat_count >= 3:
        return response
    else:
        return call_html(f"{search_term}_(satellite)")

# In case we wanna use the html response. Both look a lil hairy.


def call_html(search_term):
    """Returns response in HTML format"""

    resp = requests.get(f"{BASE_URL}{search_term}{FORMAT_PARAMETERS_HTML}").json()[
        "parse"]["text"]


def vis_sat_ids(lat, lng, alt=0, rad=70, cat=0):
    """Returns List of Sattelite Norad IDs if Visible from specified location"""
    sats = requests.get(
        f"{N2YO_BASE_URL}/above/{lat}/{lng}/{alt}/{rad}/{cat}/&apiKey={api_key}").json()
    sat_ids = [sat["satid"] for sat in sats]
    return sat_ids


def vis_sat_data(lat, lng, alt=0, rad=70, cat=0):
    """Returns List of Sattelite Norad IDs if Visible from specified location"""
    try:
        sats = requests.get(
            f"{N2YO_BASE_URL}/above/{lat}/{lng}/{alt}/{rad}/{cat}/&apiKey={api_key}").json()
        return sats
    except:
        raise Exception("API error")


def serialize_sat_data(sat):
    return {
        "sat_location": {
            "satlat": sat["satlat"],
            "satlng": sat["satlng"],
            "satalt": sat["satalt"]
        },
        "sat_info": {
            "satid": sat["satid"],
            "satname": sat["satname"],
            "launchDate": sat["launchDate"]
        }
    }


def filter_sats(search_by, search_term):
    sat = Satellite.query.filter_by(search_by=search_term).first()
    return sat


def satellite_news(page):
    """returns a list of satellite news stories"""
    stories = requests.get(f"{NEWS_BASE_URL}satellite&page={page}").json()
    return stories


def satellite_tle(norad_id):
    """returns satellite TLE data given a norad_id"""
    try:
        sat = requests.get(f"{N2YO_BASE_URL}/tle/{norad_id}&apiKey={api_key}")
        return sat
    except:
        raise Exception("API error")
