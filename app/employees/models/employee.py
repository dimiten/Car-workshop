from app.db.database import Base
from sqlalchemy import Column, String, Boolean
from uuid import uuid4


class Employee(Base):
    __tablename__ = "employees"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(50))
    surname = Column(String(50))
    email = Column(String(50), unique=True)
    phone_number = Column(String(15), unique=True)
    position = Column(String(50))
    is_admin = Column(Boolean, default=False)

    def __init__(self, name, surname, email, phone_number, position, is_admin=False):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.position = position
        self.is_admin = is_admin

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.surname != other.surname:
            return False
        if self.email != other.email:
            return False
        if self.phone_number != other.phone_number:
            return False
        if self.position != other.position:
            return False
        if self.is_admin != other.is_admin:
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
        if self.position == other.position:
            return False
        if self.is_admin == other.is_admin:
            return False
        return True
