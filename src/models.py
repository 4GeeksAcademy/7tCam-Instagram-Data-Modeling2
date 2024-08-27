import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
# para pract.
Base = declarative_base()

# tags = Table('tags',
#     Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True),
#     Column('page_id', Integer, ForeignKey('page.id'), primary_key=True)
# )

# class Page(Model):
#     id = Column(Integer, primary_key=True)
#     tags = relationship('Tag', secondary=tags, lazy='subquery',
#         backref=backref('pages', lazy=True))

# class Tag(Model):
    # id = Column(Integer, primary_key=True)
# claves foraneas
#name variable | declarando una tabla

followers = Table('followers',
    Base.metadata,
    Column('user_from_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('user_to_id', Integer, ForeignKey('user.id'), primary_key=True)
)
class Follower(Base):
    __tablename__ = 'folllowers'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)


#commet 
# class Address(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(120), nullable=False)
    # person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
    #     nullable=False)


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    commment_text = Column(String)
    #            entero       | de donde viene el id foraneo |
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post = relationship('Comment', backref='post', lazy=True)
    post = relationship('Media', backref='post', lazy=True)


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    typ = Column(Enum(),nullable=False)
    url = Column(String)
    user_id = Column(Integer, ForeignKey('post.id'), nullable=False)


# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     addresses = db.relationship('Address', backref='person', lazy=True)

# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), nullable=False)
#     person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
#         nullable=False)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    # relationship se coloca en la tabla donde esta el id principal(funcion que relaciona tablas)
    # name coherente      |nameClase donde esata la clave foranea| nombre de la tabla actual
    comment = relationship('Commet', backref='user', lazy=True)
    post = relationship('Post', backref='user', lazy=True)


    def to_dict(self):
        return {}






## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
