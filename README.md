# Adopt A Civic Art

## Description & History

This project was inspired by City of Boston's Adopt-a-Hydrant program (an Esri application with support from Code for America) where members of the community could "adopt" a hydrant and commit to shoveling snow to provide access to the hydrant for the Fire Department after every snowfall. The adopter would then be asked to submit a picture of the newly shoveled access path to the hydrant.

For civic artwork, the adoption model is different. We ABSOLUTELY do not want members of the community to remove graffiti or guano directly. In our model, the member of the community who adopts an available civic artwork is asked to take a series of documentary photos so Los Angeles County Arts Commission staff can visually monitor the works for common public art issues. The primary purpose of the adoption program is civic engagement with artworks that are part of the County civic art collection, and the secondary purpose is monitoring for maintenance and conservation issues.

The basic function of this web application is to provide a platform for community members to submit photos of County-owned civic artworks as a means of visual documentation and trigger maintenance efforts as needed.

## Technical Overview

This project is a [Django](https://www.djangoproject.com) application written in **Python 3**.<br>
For this prototyping round the database will be a local SQLite file until we change the engine to PostgreSQL to be production ready.

### Basic Prerequisites
* Python 3.4.x
* virtualenv ([virtual environment](https://docs.python.org/3/tutorial/venv.html))
* pip

There are many different ways to set up a virtual environment, so feel free to use a method that works for you. However please make sure that you are running *Python 3.4+* within the activated environment if you have multiple versions of Python on your machine.

### Install dependencies
`sudo pip3 install -r requirements.txt`

### Run migrations
`python manage.py migrate`

### Create an initial admin account
`python manage.py createsuperuser`

### Run the server locally
`python manage.py runserver`

## Setting up on Cloud9

Using Cloud9 as a standard development environment means you can avoid the issues you run into when every developer uses a different operating system, has different versions of various software, and as a result runs into different local issues.

### Set up Cloud9

Connect your GitHub account.  Fork the repo and copy the clone link.  Create a new workspace in Cloud9 and paste your clone link.

### Create a workspace

Fork the repo and then copy the SSH 


