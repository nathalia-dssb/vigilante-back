from fastapi import FastAPI
from app.api import alerts, citizens, civil_corps

app = FastAPI()

app.include_router(alerts.router, prefix="/api", tags=["alerts"])
app.include_router(citizens.router, prefix="/api", tags=["citizens"])
app.include_router(civil_corps.router, prefix="/api", tags=["civil-corps"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
