from app.db.database import Base
from sqlalchemy import Column, String, Boolean, Date
from uuid import uuid4
from datetime import date


class Customer(Base):
    __tablename__ = "customers"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    surname = Column(String(50))
    email = Column(String(50), unique=True)
    phone_number = Column(String(15), unique=True)
    date_of_registration = Column(Date)
    is_regular = Column(Boolean, default=False)

    def __init__(self, name: str, surname: str, email: str, phone_number: str,
                 date_of_registration: date, is_regular=False):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.date_of_registration = date_of_registration
        self.is_regular = is_regular

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.surname != other.surname:
            return False
        if self.email != other.email:
            return False
        if self.phone_number != other.phone_number:
            return False
        if self.date_of_registration != other.date_of_registration:
            return False
        if self.is_regular != other.is_regular:
            return False
        return True

    def __ne__(self, other):
        if self.name == other.name:
            return False
        if self.surname == other.surname:
            return False
        if self.email == other.email:
            return False
        if self.phone_number == other.phone_number:
            return False
        if self.date_of_registration == other.date_of_registration:
            return False
        if self.is_regular == other.is_regular:
            return False
        return True
