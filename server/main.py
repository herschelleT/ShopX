from fastapi import Depends, FastAPI, HTTPException, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy import func
import httpx

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from utils import crud, schemas, models
from db_manager import SessionLocal, engine

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
# from model import get_functionality, get_specs 
import uvicorn
from typing import List, Optional
import requests
import json

SECRET_KEY = "abc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

models.Base.metadata.create_all(bind=engine)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def test():
    return {"hi": "world"}

@app.post("/phones/search")
def search_phones(filters: schemas.PhoneFilter, db: Session = Depends(get_db)):
    Phone = models.Phone
    Review = models.Review
    Order = models.Order

    # Start query for filtering phones
    query = db.query(Phone)

    # Apply filters
    if filters.min_ram is not None:
        query = query.filter(Phone.ram >= filters.min_ram)
    if filters.max_ram is not None:
        query = query.filter(Phone.ram <= filters.max_ram)
    if filters.min_storage is not None:
        query = query.filter(Phone.storage >= filters.min_storage)
    if filters.max_storage is not None:
        query = query.filter(Phone.storage <= filters.max_storage)
    if filters.min_camera is not None:
        query = query.filter(Phone.camera >= filters.min_camera)
    if filters.max_camera is not None:
        query = query.filter(Phone.camera <= filters.max_camera)
    if filters.min_screen_size is not None:
        query = query.filter(Phone.screen_size >= filters.min_screen_size)
    if filters.max_screen_size is not None:
        query = query.filter(Phone.screen_size <= filters.max_screen_size)
    if filters.min_battery_capacity is not None:
        query = query.filter(Phone.battery_capacity >= filters.min_battery_capacity)
    if filters.max_battery_capacity is not None:
        query = query.filter(Phone.battery_capacity <= filters.max_battery_capacity)
    if filters.battery_rating is not None:
        query = query.filter(Phone.battery_rating == filters.battery_rating)
    if filters.min_price is not None:
        query = query.filter(Phone.price >= filters.min_price)
    if filters.max_price is not None:
        query = query.filter(Phone.price <= filters.max_price)

    # Get filtered phones
    phones = query.all()

    # Calculate the ID of phones with special attributes
    cheapest_phone = db.query(Phone.id).order_by(Phone.price.asc()).first()
    most_rated_phone = db.query(Phone.id).join(Review).group_by(Phone.id).order_by(func.avg(Review.rating).desc()).first()
    most_ordered_phone = db.query(Phone.id).join(Order).group_by(Phone.id).order_by(func.count(Order.id).desc()).first()

    # Prepare results
    return {
        "phones": phones,
        "cheapest_phone_id": cheapest_phone.id if cheapest_phone else None,
        "most_rated_phone_id": most_rated_phone.id if most_rated_phone else None,
        "most_ordered_phone_id": most_ordered_phone.id if most_ordered_phone else None
    }



@app.post("/reviews", response_model=schemas.ReviewCreate)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    # Create a new Review instance
    new_review = models.Review(
        user_id=review.user_id,
        phone_id=review.phone_id,
        laptop_id=review.laptop_id,
        rating=review.rating,
        text=review.text
    )
    
    # Add to the database
    db.add(new_review)
    db.commit()
    db.refresh(new_review)  # Refresh to get the newly created record's ID and other fields
    
    return new_review

@app.get("/reviews", response_model=List[schemas.ReviewWithUserEmail])
def get_reviews_for_device(
    phone_id: Optional[int] = Query(None), 
    laptop_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    if not phone_id and not laptop_id:
        raise HTTPException(status_code=400, detail="Either phone_id or laptop_id must be provided")

    # Query reviews based on the provided device ID, including user email
    if phone_id:
        reviews = (
            db.query(models.Review, models.User.email)
            .join(models.User, models.Review.user_id == models.User.id)
            .filter(models.Review.phone_id == phone_id)
            .all()
        )
    elif laptop_id:
        reviews = (
            db.query(models.Review, models.User.email)
            .join(models.User, models.Review.user_id == models.User.id)
            .filter(models.Review.laptop_id == laptop_id)
            .all()
        )

    # Format the response to include both review details and user email
    formatted_reviews = [
        schemas.ReviewWithUserEmail(
            id=review.Review.id,
            content=review.Review.text,
            rating=review.Review.rating,
            phone_id=review.Review.phone_id,
            laptop_id=review.Review.laptop_id,
            user_email=review.email
        )
        for review in reviews
    ]

    return formatted_reviews

@app.post("/login")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    # try: 
    db_user: models.User = crud.get_user_by_email(db, email=user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    result = pwd_context.verify(user.password, db_user.hashed_password)
    if result == True:
        return {"status": "success", "message": "Successfully logged in !", "user_id": db_user.id, "user_email": db_user.email, "type": db_user.type}
    else: 
        return {"status": "failed"}
    # except Exception as e:
    #     raise {"status": "failed"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user.password = pwd_context.hash(user.password)
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return db_user

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_email}", response_model=schemas.User)
def read_user(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email = user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/{user_id}/orders")
def read_teacher_with_classes(*, user_id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/phones")
def add_phone(phone: schemas.PhoneCreate, db: Session = Depends(get_db)):
    db_phone = crud.get_phone_by_brand_model(db, model = phone.model, brand = phone.brand).all()
    print("hi", db_phone)
    if db_phone:
        raise HTTPException(status_code=400, detail="Already registered")
    data = crud.add_phone(db, phone)
    return {
        "status": "success",
        "message": "New entry created",
        "data": data
    }

@app.get("/phones", response_model=List[schemas.PhoneResponse])
def get_all_phones(db: Session = Depends(get_db)):
    phones = db.query(
        models.Phone,
        func.avg(models.Review.rating).label("average_rating"),
        func.count(models.Order.id.distinct()).label("order_count")
    ).outerjoin(models.Review, models.Review.phone_id == models.Phone.id) \
     .outerjoin(models.Order, models.Order.phone_id == models.Phone.id) \
     .group_by(models.Phone.id) \
     .all()

    result = []
    for phone, average_rating, order_count in phones:
        phone_data = {
            **phone.__dict__,
            "average_rating": average_rating,
            "order_count": order_count
        }
        result.append(phone_data)

    return result

@app.delete("/phones/{id}")
def delete_phone(id: int, db: Session = Depends(get_db)):
    phone = db.query(models.Phone).filter(models.Phone.id == id).first()
    if phone is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Phone not found"
        )
    db.delete(phone)
    db.commit()
    return {"message": "Phone deleted successfully"}


@app.post("/orders/")
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    # Check if an order with the same user_id and phone_id already exists
    existing_order = db.query(models.Order).filter(
        models.Order.user_id == order.user_id,
        models.Order.phone_id == order.phone_id
    ).first()
    
    if existing_order:
        raise HTTPException(status_code=400, detail="Order already exists for this user and phone.")
    
    # Create a new order if no existing order is found
    new_order = models.Order(
        Brand=order.Brand,
        Model=order.Model,
        Price=order.Price,
        user_id=order.user_id,
        phone_id=order.phone_id,
        laptop_id=order.laptop_id
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    return new_order


@app.get("/orders/user/{user_id}")
def get_orders_by_user(user_id: int, db: Session = Depends(get_db)):
    orders = db.query(models.Order).filter(models.Order.user_id == user_id).all()
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found for this user")
    phones =  [order.phone for order in orders if order.phone]
    return phones

@app.post("/nlp")
async def nlp_to_query(req: Request):
    try:
        req_data = await req.json()
        user_prompt = req_data.get("user_prompt")

        instruction = """
You will be given a user request for a phone. Your task is to extract the phone specifications and return them in JSON format with min_ and max_ values for fields where applicable. If a piece of data is not available, return it as null. Your answer should be in this format i.e., JSON only. DO NOT ADD ANYTHING OTHER THAN JSON.

Format:
{
  "min_ram": null,
  "max_ram": null,
  "min_storage": null,
  "max_storage": null,
  "min_camera": null,
  "max_camera": null,
  "min_screen_size": null,
  "max_screen_size": null,
  "min_battery_capacity": null,
  "max_battery_capacity": null,
  "battery_rating": null,
  "min_price": null,
  "max_price": null
}

Examples:

Prompt: I need a phone with at least 8 GB RAM, 128 GB storage, a 48 MP camera, a 6.5-inch screen, and my budget is around $500.
Answer:
{
  "min_ram": 8,
  "max_ram": null,
  "min_storage": 128,
  "max_storage": null,
  "min_camera": 48,
  "max_camera": null,
  "min_screen_size": 6.5,
  "max_screen_size": null,
  "min_battery_capacity": null,
  "max_battery_capacity": null,
  "battery_rating": null,
  "min_price": 500,
  "max_price": 500
}

Prompt: Looking for a device with 12 GB RAM, a maximum price of $700, and excellent battery rating.
Answer:
{
  "min_ram": 12,
  "max_ram": null,
  "min_storage": null,
  "max_storage": null,
  "min_camera": null,
  "max_camera": null,
  "min_screen_size": null,
  "max_screen_size": null,
  "min_battery_capacity": null,
  "max_battery_capacity": null,
  "battery_rating": "Excellent",
  "min_price": null,
  "max_price": 700
}

Prompt:"""

        prompt = f"{instruction} '{user_prompt}'"

        url = "http://localhost:11434/api/generate"
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": "phi3.5",
            "prompt": prompt,
            "stream": False
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()
            answer = data.get("response", "No response field found.")
            # print(answer)
            json_answer = json.loads(answer)
            return JSONResponse(content={"status": "success", "answer": json_answer})

        else:
            print(f"Error: {response.status_code} - {response.text}")
            return JSONResponse(content={"status": "failure", "error": "Failed to get a valid response."}, status_code=response.status_code)

    except json.JSONDecodeError:
        return JSONResponse(content={"status": "failure", "error": "Invalid JSON format."}, status_code=400)
    except Exception as e:
        print(f"Exception: {e}")
        return JSONResponse(content={"status": "failure", "error": str(e)}, status_code=500)

# Test successful login
def test_login_success(client, test_db):
    create_test_user(test_db, "user@example.com", "password123")
    response = client.post("/login", json={"email": "user@example.com", "password": "password123"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"

# Test login failure (wrong password)
def test_login_failed_password(client, test_db):
    create_test_user(test_db, "user@example.com", "password123")
    response = client.post("/login", json={"email": "user@example.com", "password": "wrongpass"})
    assert response.status_code == 200
    assert response.json()["status"] == "failed"

# Test user not found
def test_login_user_not_found(client):
    response = client.post("/login", json={"email": "unknown@example.com", "password": "password"})
    assert response.status_code == 404
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload="true")
