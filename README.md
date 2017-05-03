
# Adopt a Civic Art
=======


## Description & History

Adopt a Civic Art serves to engage the public in the art that surrounds them throughout the county of Los Angeles while also serving as a crowd sourced monitoring tool.

This project was inspired by City of Boston's Adopt-a-Hydrant program (an Esri application with support from Code for America) where members of the community could "adopt" a hydrant and commit to shoveling snow to provide access to the hydrant for the Fire Department after every snowfall. The adopter would then be asked to submit a picture of the newly shoveled access path to the hydrant. 

For civic artwork, the adoption model is different. We ABSOLUTELY do not want members of the community to remove graffiti or guano directly. In our model, the member of the community who adopts an available civic artwork is asked to take a series of documentary photos so Los Angeles County Arts Commission staff can visually monitor the works for common public art issues. The primary purpose of the adoption program is civic engagement with artworks that are part of the County civic art collection, and the secondary purpose is monitoring for maintenance and conservation issues. 

The basic function of this web application is to provide a platform for community members to submit photos of County-owned civic artworks as a means of visual documentation and trigger maintenance efforts as needed.  


### Installation and Setup

1. `git clone https://github.com/hackforla/adopt-civic-art.git`
2. `pip install -r requirements.txt`


## Getting Started
Setup dummy database: "civicart.db"
```
python piece_sample.py
```

run app

```
python serve.py
```

Open up http://localhost:3000

### Prerequisites
Python | Flask | SQLite3 | SQLAlchemy 
