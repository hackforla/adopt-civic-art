# adopt-civic-art

## Description & History

This project was inspired by City of Boston's Adopt-a-Hydrant program (an Esri application with support from Code for America) where members of the community could "adopt" a hydrant and commit to shoveling snow to provide access to the hydrant for the Fire Department after every snowfall. The adopter would then be asked to submit a picture of the newly shoveled access path to the hydrant. 

For civic artwork, the adoption model is different. We ABSOLUTELY do not want members of the community to remove graffiti or guano directly. In our model, the member of the community who adopts an available civic artwork is asked to take a series of documentary photos so Los Angeles County Arts Commission staff can visually monitor the works for common public art issues. The primary purpose of the adoption program is civic engagement with artworks that are part of the County civic art collection, and the secondary purpose is monitoring for maintenance and conservation issues. 

The basic function of this web application is to provide a platform for community members to submit photos of County-owned civic artworks as a means of visual documentation and trigger maintenance efforts as needed.  

## Development

Having attended HackForLA for one night and am proposing web application architecture which hopefully gets adopted (haha) for the Adopt Civic Art group.
I'm starting with a Python-Flask framework serving raw HTML using SQLite DB and SqlAlchemy mapper. Currently writing database setups .py with only Piece table, mocking out Feed as landing page and Pieces as view on click, writing API and Flask routing methods.

TODO then afters:

-Styling with Bootstrap framework probably
-Adding oauth for authenification and authorization
-Incorporate logic for admin vs user for CRUD in add/delete pieces
-Add ReactJS frontend framework 

TODISCUSS need to knows:

- how to store users
- maybeeee tests?

ROUTES:
```
/
/feed
	Landing page of feed with scrolldown of pieces

/feed/<int:piece_id>
	Show that piece
=======
This project idea was initially proposed at a monthly gathering of local civic tech/data/government people, [Data + Donuts](http://datadonuts.la).  The idea was pitched at Hack For LA's 2/7/17 hack night and quickly attracted a group of interested individuals.

Since then, members have embarked on a user research phase that indudes the administering of a survey and interviews.  We are currently refining a set of required features from the results in order to develop a minimally viable product. Next steps include mocking up different versions of the app for comparison.

/feed/new
	Add piece to feed

/feed/<int:piece_id>/edit
	Edit that piece 
=======
We chose to start with a web app. DB is MySQL. Mapping is Open Streets and Leaflet. Language is Python 3. 

Using a tool like PhoneGap, we'll have the possibility of compiling to mobile later on.  

We will require temporary data storage/database solution. 

/feed/<int:piece_id>/delete
	Delete that piece

/feed/JSON
	serialize all feed into returned JSON
=======
We'll take anyone interested in joining, but we could really use additional members with skills in project management, front- and back-end development.

/feed/<int:piece_id>/JSON
	serialize piece data into returned JSON
```

DATABASE SCHEMA:
mysql://root:root@127.0.0.1:8889/civicart

Note:Using MAMP to manage MySQL server. You may have to link with:
```
ln -s /Applications/MAMP/tmp/mysql/mysql.sock /tmp/mysql.sock
```


```
Table
	Piece
		+ ID <int> primary
		+ title <string(50)> 
		+ description <string(250)>
		+ latitude <int>
		+ longitude <int>
		+ img_url <string(250)>





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
