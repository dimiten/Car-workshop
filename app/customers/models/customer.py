from app.db.database import Base
from sqlalchemy import Column, String, Boolean
from uuid import uuid4


class Customer(Base):
    __tablename__ = "customers"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    surname = Column(String(50))
    email = Column(String(50), unique=True)
    phone_number = Column(String(15), unique=True)
    is_regular = Column(Boolean, default=False)

    def __init__(self, name, surname, email, phone_number, is_regular=False):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.is_regular = is_regular
