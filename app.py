from flask import Flask, request, redirect, flash, render_template, jsonify, make_response, session
from flask_debugtoolbar import DebugToolbarExtension
from dotenv import load_dotenv
from models import db, connect_db, Satellite
from categories import categories
from werkzeug.exceptions import BadRequestKeyError


from helper import call_wikitext, parse_for_sat, vis_sat_ids, filter_sats, vis_sat_data, satellite_news, serialize_satellite, search_wiki
import os

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

connect_db(app)



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


@app.route("/satellites/api/<int:id>")
def get_one_satellite(id):
    """returns satellite data from database and results from wiki api"""
    sat = Satellite.query.get(id)
    wiki = search_wiki(id)
    try:
        serialized_sat=serialize_satellite(sat)
    except AttributeError:
        serialized_sat="not found"
    return jsonify(satellite=serialized_sat, wiki=wiki)


@app.route('/satellites/api/<lat>/<lng>/<alt>')
def get_visible_satellites(lat, lng, alt):
    """returns a dictionary of satellites  within 25 mile radius of a location """
    sats = vis_sat_data(lat, lng, alt)
    return sats

@app.route('/satellites/api/<lat>/<lng>/<alt>/<cat>')
def get_visible_satellites_categories(lat, lng, alt, cat):
    """returns a dictionary of satellites in a specified category within 25 mile radius of a location """
    sats = vis_sat_data(lat, lng, alt, cat)
    count=0
    for sat in sats['above']:
        try:
            sat_from_db=Satellite.query.get(int(sat['satid']))
            sat['category']=sat_from_db.purpose
            count+=1
        except: 
            sat['category']="unknown" 
        print(count)
    return sats



@app.route("/satellites/news")
def show_news():
    """route to show satellite news stories"""
    try:
        """saves current page to session"""
        session['curr_page'] = int(request.args['page'])
    except BadRequestKeyError:
        session['curr_page'] = 1
    """get current page and make request for news stories"""
    page = session['curr_page']
    stories = satellite_news(page)
    """pagination variables to pass into template"""
    size = int(stories['totalPages'])
    if page > size:
        page = size
    if page < 1:
        page = 1
    pages = range(page-5, page+5)
    return render_template('news.html',
                           news=stories['docs'],
                           pages=pages,
                           size=size
                           )

@app.route('/about')
def show_about():
    """Route to show About Team page"""
    return render_template('about.html')