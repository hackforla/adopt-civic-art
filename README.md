# Adopt A Civic Art

## Description & History

This project was inspired by City of Boston's Adopt-a-Hydrant program (an Esri application with support from Code for America) where members of the community could "adopt" a hydrant and commit to shoveling snow to provide access to the hydrant for the Fire Department after every snowfall. The adopter would then be asked to submit a picture of the newly shoveled access path to the hydrant.

For civic artwork, the adoption model is different. We ABSOLUTELY do not want members of the community to remove graffiti or guano directly. In our model, the member of the community who adopts an available civic artwork is asked to take a series of documentary photos so Los Angeles County Arts Commission staff can visually monitor the works for common public art issues. The primary purpose of the adoption program is civic engagement with artworks that are part of the County civic art collection, and the secondary purpose is monitoring for maintenance and conservation issues.

The basic function of this web application is to provide a platform for community members to submit photos of County-owned civic artworks as a means of visual documentation and trigger maintenance efforts as needed.

## Technical Overview

This project is a [Django](https://www.djangoproject.com) application written in **Python 3** using a _PostgreSQL_ database.<br>

## Installation Instructions
Basic Prerequisites:<br>

* Python 3.4.x
* virtualenv ([virtual environment](https://docs.python.org/3/tutorial/venv.html))
* pip

There are many different ways to set up a virtual environment, so feel free to use a method that works for you. However please make sure that you are running *Python 3.4+* within the activated environment if you have multiple versions of Python on your machine.

### Local Settings
Find the `/civicart/sample_local_settings.py` file and rename to `local_settings.py`. This configures a SQLite server and a debug environment for local development.

### Install dependencies
`sudo pip3 install -r requirements.txt`

### Run migrations
`python manage.py migrate`

### Create an initial admin account
`python manage.py createsuperuser`

### Run the server locally
`python manage.py runserver`

## Front End Development
This project uses Webpack 2 to compile JS and SCSS files.

### Install NPM dependencies
`npm install`

### Build JS/SCSS files
`npm run build`

### Watch JS/SCSS files
`npm run watch`

## Development Server
The dev server is currently hosted as a [Heroku](https://www.heroku.com/) app for ease of deployment.

### Deployment Instructions
Make sure to set environment variables for `SECRET_KEY` (random 30 character string), and `GOOGLE_MAPS_API_KEY`.

1. `heroku login`
2. Commit all production ready changes onto local git repo
3. `git push heroku master`

