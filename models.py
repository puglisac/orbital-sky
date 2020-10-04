"""Models for satellites"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Satellite(db.Model):
    """Satellite."""

    __tablename__ = "satellites"

    norad_num = db.Column(db.Integer,
                          primary_key=True
                          )
    satellite_name = db.Column(db.String
                               )
    country_of_origin = db.Column(db.String
                                  )
    country_of_owner = db.Column(db.String
                                 )
    sat_owner = db.Column(db.String
                          )
    users = db.Column(db.String
                      )
    purpose = db.Column(db.String
                        )
    purpose_detail = db.Column(db.String
                               )
    class_of_orbit = db.Column(db.String
                               )
    type_of_orbit = db.Column(db.String
                              )
    longitude_of_geo = db.Column(db.Float
                                 )
    perigee = db.Column(db.Float
                        )
    apogee = db.Column(db.Float
                       )
    eccentricity = db.Column(db.Float
                             )
    inclination = db.Column(db.Float
                            )
    sat_period = db.Column(db.Float
                           )
    launch_mass = db.Column(db.Float
                            )
    dry_mass = db.Column(db.String
                         )
    sat_power = db.Column(db.String
                          )
    launch_date = db.Column(db.DateTime
                            )
    life_expectancy = db.Column(db.Float
                                )
    contractor = db.Column(db.String
                           )
    contractor_country = db.Column(db.String
                                   )
    launch_site = db.Column(db.String
                            )
    launch_vehicle = db.Column(db.String
                               )
    cospar_num = db.Column(db.String
                           )
    comments = db.Column(db.String
                         )
    orbital_data_source = db.Column(db.String
                                    )
    source1 = db.Column(db.String
                        )
    source2 = db.Column(db.String
                        )
    source3 = db.Column(db.String
                        )
    source4 = db.Column(db.String
                        )
    source5 = db.Column(db.String
                        )
    source6 = db.Column(db.String
                        )

    

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
