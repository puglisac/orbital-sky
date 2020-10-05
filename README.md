# What's Up, Spock?

![GitHub repo code size](https://img.shields.io/github/languages/code-size/puglisac/orbital-sky)
![GitHub contributors](https://img.shields.io/github/contributors/puglisac/orbital-sky)
![GitHub stars](https://img.shields.io/github/stars/puglisac/orbital-sky?style=social)
![GitHub forks](https://img.shields.io/github/forks/puglisac/orbital-sky?style=social)

**Created by: Matt McFarland, Alan Puglisi, and James Reid**

Created for [NASA's 2020 International Space App Challenge](https://www.spaceappschallenge.org/about/), What's Up, Spock? is the ultimate tool for tracking your local satellite activity. Simply click the button and your location will be cross-referenced with multiple databases of international satellites near your current location.

Check it out here: [https://whats-up-spock.herokuapp.com/](https://whats-up-spock.herokuapp.com/)


## Technologies Used
Frontend
- JavaScript
- Bootstrap
- HTML
- CSS

Backend
- Python
- Flask
- SQLAlchemy

Database
- PostgreSQL

## Credits
- Globe visualization provided by [Nasa's WorldWind](https://worldwind.arc.nasa.gov/)
- Current satellite locations provided by [N2YO](https://www.n2yo.com/login/)
- Additional satellite info provided by the following:
  * [Union of Concerned Scientists Satellite Database](https://www.ucsusa.org/resources/satellite-database)
  * [Wikipedia](https://www.wikipedia.org/)

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have an Internet browser (Chrome, Firefox, Safari, etc)
* You have a code editor (VS Code, Atom, etc)
* You have python3 and pip

## Installation

To install, follow these steps:

Via Downloading from GitHub:
1. Download this repository onto your machine by clicking the "Clone or Download" button or Fork the repo into your own Github account
2. Download and extract the zip file to a directory of your choice.

Via command line:
```
$ git clone https://github.com/puglisac/orbital-sky.git
```


Backend Environment Setup:
1. In the directory you've cloned or downloaded the repo to, create the virtual environment and activate it

```
$ python3 -m venv venv
$ source venv/bin/activate
```

2. Install dependencies

```
(venv)$ pip3 install -r requirements.txt
```
3. [Install PostgreSQL](https://www.postgresql.org/download/) if you do not have it.

4. Create a database and seed it
```
$ createdb satellites_db
$ psql satellites_db < satellites_data.sql
```
5. Head over to [N2YO](https://www.n2yo.com/login/) and register for an account

6. Create a .env file in the backend directory and add the following environment variables.

```
SQLALCHEMY_DATABASE_URI=postgresql:///satellites_db
SECRET_KEY=<generate a random string for Flask's secret key>
n2yo_api_key=<add your key here>
```
7. Start up the Flask server
```
(venv)$ flask run
```
8. Navigate your preferred browser (Chrome suggested) to http://127.0.0.1:5000/


## Contributing

We welcome contributions! Feel free to open a PR and then reach out at the emails below.

## Support and Contact

If you want to contact us you can reach us at <mrmcfarland@gmail.com>, <alan.c.puglisi@gmail.com>, and <jreidmke@gmail.com>

## License

This project uses the following license: [MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2020 Matt McFarland