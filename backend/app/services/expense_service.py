from app.repositories.expense_repository import ExpenseRepository
from app.schemas.expense_schema import ExpenseCreate

class ExpenseService:
    def __init__(self, repo: ExpenseRepository):
        self.repo = repo

    async def create(self, data: ExpenseCreate):
        # 예: 유효성 검사, 로직 처리 등 가능
        return await self.repo.create_expense(data)

    async def get(self, income_id: str):
        return await self.repo.get_expense(income_id)

    async def update(self, income_id: str, data: ExpenseCreate):
        return await self.repo.update_expense(income_id, data)

    async def delete(self, income_id: str):
        return await self.repo.delete_expense(income_id)