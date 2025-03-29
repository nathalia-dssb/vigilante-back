from app.db.database import get_db
from bson import ObjectId
from typing import Optional, Dict, Any

db = get_db()

# Operaciones CRUD para Alertas
def create_alert(alert_data: Dict[str, Any]):
    result = db.alerts.insert_one(alert_data)
    return db.alerts.find_one({"_id": result.inserted_id})

def get_alert(alert_id: str):
    return db.alerts.find_one({"_id": ObjectId(alert_id)})

# Operaciones CRUD para Ciudadanos
def create_citizen(citizen_data: Dict[str, Any]):
    result = db.citizens.insert_one(citizen_data)
    return db.citizens.find_one({"_id": result.inserted_id})

def get_citizen(citizen_id: str):
    return db.citizens.find_one({"_id": ObjectId(citizen_id)})

# Operaciones CRUD para Cuerpo Civil
def create_civil_corps(civil_corps_data: Dict[str, Any]):
    result = db.civil_corps.insert_one(civil_corps_data)
    return db.civil_corps.find_one({"_id": result.inserted_id})

def get_civil_corps(civil_corps_id: str):
    return db.civil_corps.find_one({"_id": ObjectId(civil_corps_id)})
