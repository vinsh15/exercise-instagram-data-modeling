import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(30), nullable=False)
    user_name = Column(String(10), nullable=False)
    password = Column(String(10), nullable=False)

    posts = relationship('Post', backref="author")
    post_likes = relationship('PostLike', backref = "user")
    comments = relationship('Comment', backref = "author")
    coment_likes = relationship('CommentLike', backref = "author")
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(300), nullable=False)
    date_published = Column(DateTime, nullable=False)
    content = Column(String(300))
    latitude = Column(String(8))
    longitude = Column(String(8))
    user_id = Column(Integer, ForeignKey('user.id'))

    comments = relationship("Comment", backref = "post")
    likes = relationship("PostLike", backref = "post")

class PostLike(Base):
    __tablename__ = 'post_like'
    id = Column(Integer, primary_key=True) 
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)   
    content = Column(String(300), nullable=False)
    date_published = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    likes = relationship("ComentLike", backref = "comment")


class CommentLike(Base):
    __tablename__ = 'comment_like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')