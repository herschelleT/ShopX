from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from utils import crud, schemas, models
from db_manager import SessionLocal, engine

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from model import get_functionality, get_specs
import uvicorn

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

@app.post("/login")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    result = pwd_context.verify(user.password, db_user.hashed_password)
    # return {"raw": raw, "og": user.password, "db_pass": db_user.hashed_password}
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    elif result == True:
        return {"status": "success", "message": "Successfully logged in !", "user_id": db_user.id, "user_email": db_user.email}
    else:
        raise HTTPException(status_code=404, detail="Incorrect password")

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
    db_phone = crud.get_phone_by_brand_model(db, model = phone.Model, brand = phone.Brand)
    if db_phone is None:
        raise HTTPException(status_code=400, detail="Already registered")
    data = crud.add_phone(db, phone)
    return {
        "status": "success",
        "message": "New entry created",
        "data": data
    }

@app.post("/orders/")
def create_order(order: schemas.OrderCreate,  db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == order.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_order = models.Order(**order.dict())
    user.orders.append(new_order)
    db.add(new_order)
    db.commit()
    db.refresh(new_order) 
    return new_order

@app.post("/")
async def get(req: Request):
    req = await req.json()
    text = req["body"]
    response = get_specs(text)
    return response

@app.post("/fetch")
async def fetch_result(req: Request, db:Session =  Depends(get_db)):
    req = await req.json()
    device = req["device"]
    specifications: dict = req["specifications"]
    try:
        query = db.query(models.Phone) #make this dynamic !!!!
        for key, value in specifications.items():
            column_name, operator = key.split('_')
            column_attr = getattr( models.Phone, column_name)
            if operator == '<':
                query = query.filter(column_attr < value)
            elif operator == '>':
                query = query.filter(column_attr > value)
            elif operator == '>=':
                query = query.filter(column_attr >= value)
            else:
                query = query.filter(column_attr == value)  


        results = query.all()
        return {
            "status": "success",
            "data": results,
        }
    except Exception as e:
        print(e)

# @app.post("/fetch")
# async def fetch_result(req: Request):
#     req = await req.json()
#     device = req["device"]
#     specifications = req["specifications"]
#     try:
#         mycon = mariadb.connect(
#             user="root",
#             password="123",
#             host="127.0.0.1",
#             database="shop"
#         )
#         mycursor = mycon.cursor()
#         # query="SELECT ID,Brand,Model,RAM,Storage,Screen_Size,Camera,Battery,Storage,Price FROM phones where Price<{} and Type='{}'".format(
#         # budget,type)
#         query  = "SELECT * FROM "
#         query += device + "s WHERE "
#         for key, value in specifications.items():
#             clause = key +  value
#             query += " " + clause + " AND "
#         query += "1"
#         mycursor.execute(query)
#         myresult = mycursor.fetchall()
#         # print(myresult)
#         # create query here

#         # if mycursor.rowcount==0:
#         #     print("No such devices found.")
#         # else:
#         #     print(tabulate(myresult, headers=['ID','Brand','Model','RAM','Storage','Screen Size','Camera','Battery','Storage','Price'], tablefmt='fancy_grid'))
#         #     add_to_cart('phones', budget, type)
#         #     mycursor = mycon.cursor()

#         return {
#             "status": "success",
#             "data": myresult
#         }

#     except mariadb.Error as e:
#         return {
#             "status": "success",
#             "message": e
#         }



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload="true")
