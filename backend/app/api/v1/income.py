from fastapi import APIRouter, Depends
from app.schemas.income_schema import IncomeCreate, IncomeOut
from app.services.income_service import IncomeService
from app.database import get_database  # DB 종속성 주입
from app.repositories.income_repository import IncomeRepository
from typing import List

router = APIRouter()

def get_income_service(db=Depends(get_database)):
    repo = IncomeRepository(db)
    return IncomeService(repo)

@router.post("/", response_model=str)
async def create_income(data: IncomeCreate, service=Depends(get_income_service)):
    return await service.create(data)

@router.get("/", response_model=List[IncomeOut])
async def get_all_incomes(service=Depends(get_income_service)):
    return await service.get_all()

@router.get("/{income_id}", response_model=IncomeOut)
async def get_income(income_id: str, service=Depends(get_income_service)):
    return await service.get(income_id)

@router.put("/{income_id}", response_model=IncomeOut)
async def update_income(income_id: str, data: IncomeCreate, service=Depends(get_income_service)):
    return await service.update(income_id, data)

@router.delete("/{income_id}")
async def delete_income(income_id: str, service=Depends(get_income_service)):
    return await service.delete(income_id)
