from sqlalchemy import Column, String, Integer, orm, Enum
from sqlalchemy.orm import relationship

from app.models.base import Base
from flask_login import UserMixin
from app.models.base import db
import bcrypt


class User(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100))
    _password = Column('password', String(200))
    utype = Column(Enum('Teacher', 'Student', 'Admin'), nullable=False)
    requests = relationship("Request", back_populates="user", cascade="all, delete-orphan")
    experiments = relationship("Experiment", back_populates="user", cascade="all, delete-orphan")

    def __init__(self, email, password, utype):
        super().__init__()
        self.email = email
        self.password = password
        self.utype = utype

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self._password.encode('utf-8'))

    def __repr__(self):
        return f"<User id={self.id} email={self.email} type={self.utype}>"
