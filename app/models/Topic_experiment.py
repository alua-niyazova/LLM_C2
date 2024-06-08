from sqlalchemy import Column, String, Integer, orm, Float
from app.models.base import Base  # 用于在不同模块之间共享类


class Topic_experiment(Base):
    __tablename__ = 'Topic_experiment'
    eid = Column(Integer, primary_key=True, autoincrement=True)
    vTxt = Column(String(100))
    LLMused = Column(String(100))  # 确保数据库表的列名就是 "LLMused"
    answer = Column(String(100))
    score = Column(Float)

    def __init__(self, vTxt, LLMused, answer, score):
        super(Topic_experiment, self).__init__()
        # self.questionName = qCode
        self.vTxt = vTxt
        self.LLMused = LLMused
        self.answer = answer
        self.score = score
