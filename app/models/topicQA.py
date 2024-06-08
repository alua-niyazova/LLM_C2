from sqlalchemy import Column, String, Integer, orm
from app.models.helpTopicElement import HelpTopicElement

class TopicQA(HelpTopicElement):
    topicQ = Column(String(100))
    topicA = Column(String(100))

    def __init__(self, title, topicid, q, a):
        super().__init__(title, topicid)
        self.topicQ = q
        self.topicA = a