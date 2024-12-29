from sqlalchemy import Column, Integer, String, Boolean, ForeignKey 
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='true', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    """ to define rollback condition if user enters invalid content to further prevent the count of id to original one"""


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable= False, unique=True )    
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

    """ to define rollback condition if user enters invalid content to further prevent the count of id to original one"""


class Vote(Base):
    __tablename__ = "votes"

    post_id = Column(Integer, ForeignKey("posts.id", ondelete="Cascade"), nullable=False, primary_key=True,)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="Cascade"), primary_key=True, nullable=False)

    


