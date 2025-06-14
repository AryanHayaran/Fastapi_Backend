from pydantic import BaseModel, Field
from datetime import datetime
import uuid
from typing import Optional, List

class ReviewModel(BaseModel):
    uid: uuid.UUID
    rating: int = Field(lt=5)
    review_text: str
    user_uid: Optional[uuid.UUID] 
    book_uid: Optional[uuid.UUID] 
    created_at: datetime 
    updated_at: datetime 

class ReviewCreateModel(BaseModel):
    rating: int = Field(lt=5)
    review_text: str