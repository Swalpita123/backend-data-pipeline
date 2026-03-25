from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models.customer import Customer
from services.ingestion import ingest_data
from database import Base
import time

app = FastAPI()

# wait for postgres to be ready
for i in range(10):
    try:
        Base.metadata.create_all(bind=engine)
        print("Database connected")
        break
    except Exception as e:
        print("Waiting for database...")
        time.sleep(3)


@app.post("/api/ingest")
def ingest():
    db: Session = SessionLocal()
    processed = ingest_data(db)

    return {
        "status": "success",
        "records_processed": processed
    }


@app.get("/api/customers")
def get_customers(page: int = 1, limit: int = 10):

    db = SessionLocal()

    start = (page - 1) * limit

    customers = db.query(Customer).offset(start).limit(limit).all()

    return customers


@app.get("/api/customers/{customer_id}")
def get_customer(customer_id: str):

    db = SessionLocal()

    customer = db.query(Customer).filter_by(customer_id=customer_id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer