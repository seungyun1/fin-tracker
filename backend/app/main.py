from fastapi import FastAPI
from api.v1 import income, expense

app = FastAPI()

app.include_router(income.router, prefix="/api/v1/incomes", tags=["Income"])
# app.include_router(expense.router, prefix="/api/v1/expenses", tags=["Expense"])