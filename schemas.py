from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

# ... other Pydantic models for Token, Story, etc. ...
