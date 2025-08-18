from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.income_model import build_income_dict
from datetime import datetime

class IncomeRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["incomes"]

    async def create_income(self, data):
        income = build_income_dict(data)
        result = await self.collection.insert_one(income)
        return str(result.inserted_id)

    async def get_income(self, income_id):
        return await self.collection.find_one({"_id": ObjectId(income_id)})

    async def update_income(self, income_id, data):
        update_data = data.dict()
        update_data["updated_at"] = datetime.utcnow()
        await self.collection.update_one(
            {"_id": ObjectId(income_id)},
            {"$set": update_data}
        )

    async def delete_income(self, income_id):
        await self.collection.delete_one({"_id": ObjectId(income_id)})