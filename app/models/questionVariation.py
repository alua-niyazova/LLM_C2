from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class QuestionVariation(Base):
    __tablename__ = 'question_variation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vCode = Column(String(100))  # variation question code
    vText = Column(String(200))  # variation question text
    question_id = Column(Integer, ForeignKey('assignQ.id'))
    question = relationship("AssignQ", back_populates="variations")
    answers = relationship("LLMAnswer", back_populates="variation", cascade="all, delete-orphan")

    def __init__(self, vcode, vtext, question_id):
        super(QuestionVariation, self).__init__()
        self.vCode = vcode
        self.vText = vtext
        self.question_id = question_id
