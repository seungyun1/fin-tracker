from repositories.income_repository import IncomeRepository
from schemas.income_schema import IncomeCreate

class IncomeService:
    def __init__(self, repo: IncomeRepository):
        self.repo = repo

    async def create(self, data: IncomeCreate):
        # 예: 유효성 검사, 로직 처리 등 가능
        return await self.repo.create_income(data)

    async def get(self, income_id: str):
        return await self.repo.get_income(income_id)

    async def update(self, income_id: str, data: IncomeCreate):
        return await self.repo.update_income(income_id, data)

    async def delete(self, income_id: str):
        return await self.repo.delete_income(income_id)