from fastapi import APIRouter, Depends
from schemas.income_schema import IncomeCreate, IncomeOut
from services.income_service import IncomeService
from database import get_database  # DB 종속성 주입
from repositories.income_repository import IncomeRepository

router = APIRouter()

def get_income_service(db=Depends(get_database)):
    repo = IncomeRepository(db)
    return IncomeService(repo)

@router.post("/", response_model=str)
async def create_income(data: IncomeCreate, service=Depends(get_income_service)):
    return await service.create(data)

@router.get("/{income_id}", response_model=IncomeOut)
async def get_income(income_id: str, service=Depends(get_income_service)):
    return await service.get(income_id)