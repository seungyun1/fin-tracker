from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class IncomeBase(BaseModel):
    amount: float
    category: str
    description: Optional[str]
    date: datetime

class IncomeCreate(IncomeBase):
    pass

class IncomeOut(IncomeBase):
    id: str
    created_at: datetime
    updated_at: datetime

    # class Config:
    #     orm_mode = True