from flask import Flask, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Satellite

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
    """Homepage"""

    return


##############################################################################


@app.route("/satellites")
def show_all_satellites():

    satellites = Satellite.query.all()


@app.route("/satellites/<int:id>")
def show_one_satellite(id):

    satellite = Satellite.query.filter_by(norad_num=id).first()
    print("******************", satellite.satellite_name)
