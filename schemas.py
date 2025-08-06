from pydantic import BaseModel
from typing import Optional
import uuid

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    username: str

class UserLogin(BaseModel):
    email: str
    password: str

class User(UserBase):
    id: uuid.UUID
    is_premium: bool
    credits_remaining: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class StoryPrompt(BaseModel):
    prompt_text: str

class Story(BaseModel):
    id: uuid.UUID
    title: str
    cover_image_url: Optional[str] = None
    author_id: uuid.UUID
    status: str
    class Config:
        orm_mode = True
