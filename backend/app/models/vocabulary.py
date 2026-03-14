from sqlalchemy import Column,String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.db import Base

class Vocabulary(Base):

__tablename__="vocabulary"

id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
term = Column(String)
enterprise_meaning = Column(String)
department = Column(String)
