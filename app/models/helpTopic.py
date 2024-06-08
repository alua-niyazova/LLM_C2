from sqlalchemy import Column, String, Integer, ForeignKey
from app.models.base import Base  # 用于在不同模块之间共享类
from sqlalchemy.orm import relationship
class Helptopic(Base):
    __tablename__ = 'helptopic'
    coursetype =Column(String(30))
    topicid = Column(Integer, primary_key=True, autoincrement=True, comment='ID')
    topic = Column(String(50))
    subtopic = Column(String(50))
    topicq = Column(String(100))
    topica = Column(String(100))
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship("Course", back_populates="helptopics")

    def __init__(self, topic, subtop, coursetype,topicq, topica,course_id):
        super(Helptopic, self).__init__()
        self.topic = topic
        self.subtopic = subtop
        self.coursetype = coursetype
        self.topicq = topicq
        self.topica = topica
        self.course_id = course_id

