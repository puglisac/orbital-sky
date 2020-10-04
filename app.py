from flask import Flask, request, redirect, flash, render_template, jsonify, make_response
from flask_debugtoolbar import DebugToolbarExtension
from dotenv import load_dotenv
from models import db, connect_db, Satellite
from categories import categories

from helper import call_wikitext, parse_for_sat, vis_sat_ids, filter_sats, vis_sat_data, serialize_sat_data
import os

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

connect_db(app)
db.create_all()


# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage"""

    return render_template('app.html')


##############################################################################


@app.route("/satellites")
def show_all_satellites():
    satellites = Satellite.query.all()


@app.route("/satellites/<int:id>")
def show_one_satellite(id):
    satellite = Satellite.query.get(id)

@app.route('/satellites/api/<lat>/<lng>/<alt>/<rad>')
def get_visible_satellites(lat, lng, alt, rad): 
    if not request.json['category']:
        sats = vis_sat_data(lat, lng, alt, rad)
        return sats
    else:
        cat=categories[request.json['category']]   
        sats = vis_sat_data(lat, lng, alt, rad, cat)
        return sats
