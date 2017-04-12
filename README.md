# ADOPT CIVIC ART PROJECT 

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

/feed/new
	Add piece to feed

/feed/<int:piece_id>/edit
	Edit that piece 

/feed/<int:piece_id>/delete
	Delete that piece

/feed/JSON
	serialize all feed into returned JSON

/feed/<int:piece_id>/JSON
	serialize piece data into returned JSON
```

DATABASE SCHEMA: 
sqlite:///civicart.db
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