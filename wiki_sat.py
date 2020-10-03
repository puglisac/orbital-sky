"""Makes a call using sat name and returns the wiki page content"""

from flask import Flask
import requests

BASE_URL = "https://en.wikipedia.org/w/api.php?action=parse&page="

FORMAT_PARAMETERS_HTML = "&format=json&prop=text&formatversion=2"
FORMAT_PARAMETERS_WIKITEXT = "&format=json&prop=wikitext&formatversion=2"

def call_wikitext(search_term):
    """Returns response in WikiText format. If response is error, returns list of USA Satellites"""

    resp = requests.get(f"{BASE_URL}{search_term}{FORMAT_PARAMETERS_WIKITEXT}").json()
    if "error" in resp:
        return requests.get(f"{BASE_URL}List_of_USA_satellites{FORMAT_PARAMETERS_WIKITEXT}").json()["parse"]["wikitext"]
    else:
        return parse_for_sat(resp['parse']['wikitext'], search_term)


def parse_for_sat(response, search_term):
    sat_count = response.count('atellite')
    if sat_count >= 3:
        return response
    else:
        return call_html(f"{search_term}_(satellite)")

#In case we wanna use the html response. Both look a lil hairy.

def call_html(search_term):
    """Returns response in HTML format"""

    resp = requests.get(f"{BASE_URL}{search_term}{FORMAT_PARAMETERS_HTML}").json()["parse"]["text"]
