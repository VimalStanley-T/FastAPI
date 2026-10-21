from sqlalchemy import Column, Integer, String, Boolean #Field Types
from database import Base;

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False) # value illana error through aagum.
    description = Column(String) # Ithula default ta null la iruintha problem illa.
    completed = Column(Boolean, default=False)