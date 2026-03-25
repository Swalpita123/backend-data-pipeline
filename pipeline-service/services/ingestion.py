import requests
from sqlalchemy.orm import Session
from models.customer import Customer

MOCK_API = "http://mock-server:5000/api/customers"


def ingest_data(db: Session):

    page = 1
    limit = 10
    total_processed = 0

    while True:

        response = requests.get(MOCK_API, params={"page": page, "limit": limit})
        data = response.json()

        customers = data["data"]

        if not customers:
            break

        for c in customers:

            existing = db.query(Customer).filter_by(customer_id=c["customer_id"]).first()

            if existing:
                for key, value in c.items():
                    setattr(existing, key, value)
            else:
                new_customer = Customer(**c)
                db.add(new_customer)

            total_processed += 1

        db.commit()

        page += 1

    return total_processed