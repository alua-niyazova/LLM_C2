from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.orm import relationship
from app.models.base import Base
import enum


class CourseCategory(enum.Enum):
    COMP = "Comp"
    MATH = "Math"
    WRIT = "Writ"


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cName = Column(String(50))
    cNumber = Column(Integer)
    category = Column(Enum(CourseCategory), nullable=False)
    questions = relationship("AssignQ", back_populates="course", cascade="all, delete-orphan")
    helptopics = relationship("Helptopic", back_populates="course")

    def __init__(self, name, num, cat):
        super(Course, self).__init__()
        self.cName = name
        self.cNumber = num
        self.category = cat
