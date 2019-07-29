from knowledge_model import Base, Animal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name,life_span,has_wings,rating):
	add_article1 = Animal(name=name,
		life_span=life_span, 
		has_wings=has_wings,
		rating=rating)
	session.add(add_article1)
	session.commit()
add_article("elephant",60,False,6)
add_article("horse",100,False,9)

def query_all_articles():
	animal_all=session.query(Animal).all()
	return animal_all

print(query_all_articles())



def query_article_by_topic(topic):
	chosen_topic=session.query(Animal).filter_by(name=topic).all()
	return chosen_topic

print(query_article_by_topic("elephant"))


def delete_article_by_topic(name):
	session.query(Animal).filter_by(
       name=name).delete()
	session.commit()
delete_article_by_topic("elephant")

def delete_all_articles():
	pass

def edit_article_rating():
	pass
