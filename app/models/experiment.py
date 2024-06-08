import enum

from sqlalchemy import Column, String, Integer, orm, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.models.base import Base


class ExperimentStatus(enum.Enum):
    IN_GENERAL_DATABASE = "in_general_database"
    SUBMITTED = "submitted"
    NOT_SUBMITTED = "not_submitted"


class Experiment(Base):
    __tablename__ = 'experiments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vCode = Column(String(100))
    vText = Column(String(100))
    LLM_name = Column(String(100))
    score = Column(Integer)
    comment = Column(String(100))
    status = Column(Enum(ExperimentStatus), default=ExperimentStatus.NOT_SUBMITTED, nullable=False)
    answer_img = Column(String(100))

    question_id = Column(Integer, ForeignKey('assignQ.id'))
    question = relationship("AssignQ", back_populates="experiments")
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="experiments")

    def __init__(self, question_id, vCode, vText, LLM_name, score, comment, answer_img, user_id):
        super(Experiment, self).__init__()
        self.question_id = question_id
        self.vCode = vCode
        self.vText = vText
        self.LLM_name = LLM_name
        self.score = score
        self.comment = comment
        self.answer_img = answer_img
        self.user_id = user_id


