from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import income, expense

app = FastAPI()

# CORS 설정 (React 프론트엔드와 통신을 위해)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 개발 서버 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(income.router, prefix="/api/v1/incomes", tags=["Income"])
app.include_router(expense.router, prefix="/api/v1/expenses", tags=["Expense"])
