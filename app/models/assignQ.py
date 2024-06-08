from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class AssignQ(Base):
    __tablename__ = 'assignQ'
    id = Column(Integer, primary_key=True, autoincrement=True)
    qCode = Column(String(100))  # question code
    qText = Column(String(200))  # question text
    course_id = Column(Integer, ForeignKey('course.id'))  # ForeignKey to Course
    course = relationship("Course", back_populates="questions")
    variations = relationship("QuestionVariation", back_populates="question", cascade="all, delete-orphan")
    experiments = relationship("Experiment", back_populates="question", cascade="all, delete-orphan")

    def __init__(self, qcode, qtext, course_id):
        super(AssignQ, self).__init__()
        self.qCode = qcode
        self.qText = qtext
        self.course_id = course_id
