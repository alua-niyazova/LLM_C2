from sqlalchemy import Column, String, Integer, orm, Enum, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.models.base import Base
import enum


class RequestType(enum.Enum):
    ADD_COURSE = "ADD_COURSE"
    ADD_QUESTION = "ADD_QUESTION"
    UPDATE_SCORE = "UPDATE_SCORE"
    EXPERIMENT = "EXPERIMENT"
    ADD_TOPIC = "ADD_TOPIC"


class Status(enum.Enum):
    PASSED = "passed"
    REJECTED = "rejected"
    PENDING = "pending"


class Request(Base):
    __tablename__ = 'request'
    id = Column('rid', Integer, primary_key=True, autoincrement=True)
    request_type = Column(Enum(RequestType), nullable=False)

    # following columns serves multipurpose for different request types
    col1 = Column(String(300))  # course_name/question_number/answer_id/question_id
    col2 = Column(String(300))  # course_number/question_text/new_score/new_variation_number
    col3 = Column(String(300))  # course_category/course_id/new_comment/new_variation_text
    col4 = Column(String(300))  # 0 or null/0 or null/0 or null/llm_name
    col5 = Column(String(300))  # 0 or null/0 or null/0 or null/score
    col6 = Column(String(300))  # 0 or null/0 or null/0 or null/comment
    col7 = Column(String(300))  # 0 or null/0 or null/0 or null/answer_img
    col8 = Column(String(300))  # 0 or null/0 or null/0 or null/exp_id

    status = Column(Enum(Status), default=Status.PENDING, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates="requests")

    def __init__(self, request_type, user_id, col1, col2, col3, col4=None, col5=None, col6=None, col7=None, col8=None):
        self.request_type = request_type
        self.user_id = user_id
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.col4 = col4
        self.col5 = col5
        self.col6 = col6
        self.col7 = col7
        self.col8 = col8
