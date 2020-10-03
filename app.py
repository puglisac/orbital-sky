from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Satellite
from helper import call_wikitext, parse_for_sat, vis_sat_ids, filter_sats

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///satellites_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return


##############################################################################
# Playlist routes


@app.route("/satellites")
def show_all_playlists():
    """Return a list of playlists."""

    satellites = Satellite.query.all()
    print(satellites)

@app.route('/satellites/api/<int:lat>/<int:lgn>/<int:alt>/<int:rad>')
def get_visible_satellites(lat, lgn, alt, rad):
    