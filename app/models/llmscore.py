from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class LLMScore(Base):
    __tablename__ = 'llmscore'
    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Integer)
    comment = Column(String(200))
    answer_id = Column(Integer, ForeignKey('llmanswer.id'))
    answer = relationship("LLMAnswer", back_populates="scores")
    teacher_id = Column(Integer, ForeignKey('user.id'))
    teacher = relationship("User")

    def __init__(self, score, comment, answer_id, teacher_id):
        super(LLMScore, self).__init__()
        self.score = score
        self.comment = comment
        self.answer_id = answer_id
        self.teacher_id = teacher_id

