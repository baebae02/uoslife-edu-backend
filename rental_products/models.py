from flask_sqlalchemy import Model
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey, String, Column, Unicode, DateTime, Boolean
from rental_products import db


class User(db.Model):
    id = Column(Unicode, primary_key=True)
    nickname = Column(String(50), nullable=False)
    is_admin = Column(Boolean, nullable=False)
    created_at = Column(DateTime(), nullable=False)
    updated_at = Column(DateTime(), nullable=True)
    deleted_at = Column(DateTime(), nullable=True)


class Products(db.Model):
    id = Column(Unicode, primary_key=True)
    nickname = Column(String(50), nullable=False)
    category = Column(String(50), nullable=True)
    admin_id = Column(Unicode, ForeignKey('user.id', ondelete='CASCADE'))
    student_id = Column(Unicode, ForeignKey('user.id', ondelete='CASCADE'))
    admin = relationship('User', backref=backref('product_list', order_by=id))
    student = relationship('User', backref=backref('rental_list', order_by=id))
    created_at = Column(DateTime(), nullable=False)
    updated_at = Column(DateTime(), nullable=True)
    deleted_at = Column(DateTime(), nullable=True)
    borrowed_at = Column(DateTime(), nullable=True)
    returned_at = Column(DateTime(), nullable=True)