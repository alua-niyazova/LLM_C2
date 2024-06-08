from sqlalchemy import Column, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship
from app.models.base import Base, db
from app.models.llmscore import LLMScore


class LLMAnswer(Base):
    __tablename__ = 'llmanswer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    _LLM_Name = Column(String(50))
    _LLMAnswerImg = Column(String(200))  # path to the image or URI
    _answerID = Column(String(50), unique=True)
    variation_id = Column(Integer, ForeignKey('question_variation.id'))
    variation = relationship("QuestionVariation", back_populates="answers")
    scores = relationship("LLMScore", back_populates="answer", cascade="all, delete-orphan")

    def __init__(self, name, img, variation_id):
        super(LLMAnswer, self).__init__()
        self._LLM_Name = name
        self._LLMAnswerImg = img
        self.variation_id = variation_id

    def get_llm_name(self):
        return self._LLM_Name

    def average_score(self):
        return db.session.query(func.avg(LLMScore.score)).filter(LLMScore.answer_id == self.id).scalar()
