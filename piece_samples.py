from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Piece, Base

engine = create_engine('mysql://root:root@127.0.0.1:8889/civicart')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Sample data for database to test on functionality
# Add Pieces
# TODO make better mocks with real examples

session.add(Piece(
       title="Piece 1", 
       description="description of piece 1 here", 
       latitude=0,
       longitude=0,
       img_url=""
))


session.add(Piece(
       title="Piece 2", 
       description="description of piece 2 here", 
       latitude=0,
       longitude=0,
       img_url=""
))

session.add(Piece(
       title="Piece 3", 
       description="description of piece 3 here", 
       latitude=0,
       longitude=0,
       img_url=""
))

session.add(Piece(
       title="Piece 4", 
       description="description of piece 4 here", 
       latitude=0,
       longitude=0,
       img_url=""
))

session.add(Piece(
       title="Piece 5", 
       description="description of piece 5 here", 
       latitude=0,
       longitude=0,
       img_url=""
))

session.commit()


print "added pieces!"
