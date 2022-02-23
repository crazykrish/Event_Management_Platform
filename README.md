<h1 align="center">Welcome to Event Management Platform 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: Free" src="https://img.shields.io/badge/License-Free-yellow.svg" />
  </a>
  <a href="https://twitter.com/Crazykrishnahm" target="_blank">
    <img alt="Twitter: Crazykrishnahm" src="https://img.shields.io/twitter/follow/Crazykrishnahm.svg?style=social" />
  </a>
</p>

> Rest API built for Event Management Platform

### ✨ [Demo-Click to View](https://event-management-platform-ck.herokuapp.com/)

## Technologies used

* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[PyCharm](https://www.jetbrains.com/pycharm/)** – The Python IDE for Professional Developers.
* **[Gunicorn](https://gunicorn.org/)**-Python WSGI HTTP Server for UNIX. It's a pre-fork worker model.
* **[Heroku](https://dashboard.heroku.com/apps)**-This project is hosted on this cloud platform.
* Minor dependencies can be found in the requirements.txt file on the root folder.

### Simple Model Design
<img alt="Version" src="https://user-images.githubusercontent.com/36634269/155420916-1a6fa744-fb38-4cb9-9f4e-553db9970265.png" width=300px />

### Usage
**Request[GET]**: “To View Welcome Page"<br/>
**Method**: Enter https://event-management-platform-ck.herokuapp.com/ support into address bar.<br/>
**Response**: The Welcome message page loads.<br/>

**Request [GET]**: “To View List of Entries”<br/>
**Method**: Enter https://event-management-platform-ck.herokuapp.com/events support into address bar.<br/>
**Response**: The Event List page loads.<br/>

**Request [GET]**: “To View paritcular event Data”<br/>
**Method**: Enter https://event-management-platform-ck.herokuapp.com/events/0  into address bar, you can enter 0-8 numbers <br/>
**Response**: The Particular Event Data page loads.<br/>

**Request [GET]**: “To View upcoming events Data”<br/>
**Method**: Enter https://event-management-platform-ck.herokuapp.com/events/upcoming  into address bar. <br/>
**Response**: The upcoming Event Data page loads.<br/>

**Request [GET]**: “To View Live events Data”<br/>
**Method**: Enter https://event-management-platform-ck.herokuapp.com/events/live  into address bar. <br/>
**Response**: The Live Event Data page loads, so when your current time is 10 mins away from the event time you can view this data.<br/>


### We can use database also and with slight modifications is reaquired by creating as class & post functions for it.
* **[SQLAlchemy](https://www.sqlalchemy.org/)**- The Python SQL Toolkit and Object Relational Mapper
* **[Marshmallow](https://marshmallow.readthedocs.io/en/stable/)**-simplified object serialization

## Author

👤 **Krishna H M(Crazykrish)**

* Website: https://www.linkedin.com/in/krishnahmcrazykrish/
* Twitter: [@Crazykrishnahm](https://twitter.com/Crazykrishnahm)
* Github: [@crazykrish](https://github.com/crazykrish)
* LinkedIn: [@krishnahmcrazykrish](https://linkedin.com/in/krishnahmcrazykrish)

## Show your support

Give a ⭐️ if this project helped you!
