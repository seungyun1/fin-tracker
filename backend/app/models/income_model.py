from datetime import datetime

def build_income_dict(data):
    return {
        "amount": data.amount,
        "category": data.category,
        "description": data.description,
        "date": data.date,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }