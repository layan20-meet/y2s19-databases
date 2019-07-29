from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Animal(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__='animals'
	animals_type_number=Column(Integer, primary_key=True)
	name = Column(String)
	life_span=Column(Integer)
	has_wings=Column(Boolean)
	rating=Column(Integer)

	def __repr__(self):
		return ("Animal Type: {}\n"
				"Animal Life Span: {} \n"
				"Has Wings?: {}\n"
				"Rating: {}").format(
                    self.name, self.life_span, self.has_wings, self.rating)


	