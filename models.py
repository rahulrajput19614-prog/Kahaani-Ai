from sqlalchemy import Boolean, Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, UUID
import uuid
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    auth_provider = Column(String)
    credits_remaining = Column(Integer, default=10)
    is_premium = Column(Boolean, default=False)
    stories = relationship("Story", back_populates="author")

class Story(Base):
    __tablename__ = "stories"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True)
    content = Column(JSONB)
    cover_image_url = Column(String)
    status = Column(String, default='draft')
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    author = relationship("User", back_populates="stories")
