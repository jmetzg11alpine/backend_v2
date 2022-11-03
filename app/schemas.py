from pydantic import BaseModel 

class Quiz(BaseModel):
    name: str 
    score: int 