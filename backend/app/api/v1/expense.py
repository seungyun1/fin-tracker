from fastapi import APIRouter, Depends
from app.schemas.expense_schema import ExpenseCreate, ExpenseOut
from app.services.expense_service import ExpenseService
from app.database import get_database
from app.repositories.expense_repository import ExpenseRepository
from typing import List

router = APIRouter()

def get_expense_service(db=Depends(get_database)):
    repo = ExpenseRepository(db)
    return ExpenseService(repo)

@router.post("/", response_model=str)
async def create_expense(data: ExpenseCreate, service=Depends(get_expense_service)):
    return await service.create(data)

@router.get("/{expense_id}", response_model=ExpenseOut)
async def get_expense(expense_id: str, service=Depends(get_expense_service)):
    return await service.get(expense_id)

@router.get("/", response_model=List[ExpenseOut])
async def get_all_expenses(service=Depends(get_expense_service)):
    return await service.get_all()

@router.put("/{expense_id}", response_model=ExpenseOut)
async def update_expense(expense_id: str, data: ExpenseCreate, service=Depends(get_expense_service)):
    return await service.update(expense_id, data)

@router.delete("/{expense_id}")
async def delete_expense(expense_id: str, service=Depends(get_expense_service)):
    return await service.delete(expense_id)
