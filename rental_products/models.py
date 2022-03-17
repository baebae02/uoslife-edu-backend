from sqlalchemy import ForeignKey, String, Column,DateTime, Boolean
from sqlalchemy_utils import UUIDType
from rental_products import db
import uuid


class User(db.Model):
    __table_name__ = 'user'
    id = Column(UUIDType, primary_key=True, nullable=False, default=uuid.uuid4)
    nickname = Column(String(50), nullable=False)
    is_admin = Column(Boolean, nullable=False)
    created_at = Column(DateTime(), nullable=True)
    updated_at = Column(DateTime(), nullable=True)
    deleted_at = Column(DateTime(), nullable=True)


class Product(db.Model):
    __table_name__ = 'product'
    id = Column(UUIDType, primary_key=True, nullable=False)
    nickname = Column(String(50), nullable=False)
    category = Column(String(50), nullable=True)
    admin_id = Column(UUIDType, ForeignKey('user.id', ondelete='CASCADE'))
    student_id = Column(UUIDType, ForeignKey('user.id', ondelete='CASCADE'))
    created_at = Column(DateTime(), nullable=True)
    updated_at = Column(DateTime(), nullable=True)
    deleted_at = Column(DateTime(), nullable=True)
    borrowed_at = Column(DateTime(), nullable=True)
    returned_at = Column(DateTime(), nullable=True)