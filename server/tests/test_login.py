import pytest
from fastapi.testclient import TestClient
from fastapi import Depends
from main import app, get_db
from utils import crud, schemas
from sqlalchemy.orm import Session
from db_manager import SessionLocal
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@pytest.fixture(scope="module")
def client():
    def override_get_db():
        db = SessionLocal()  
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db  
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()  

def test_login_success(client):
    db = next(get_db())  
    try:
        test_user = schemas.UserCreate(
            email="testuser@example.com",
            password= pwd_context.hash("1234"),
            type="regular"
        )
        crud.create_user(db, user=test_user)
    finally:
        db.close() 

    login_data = {
        "email": "testuser@example.com",
        "password": "1234"
    }
    response = client.post("/login", json=login_data)
    print("hiii", response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_login_failed(client):
    db = next(get_db())  
    try:
        test_user = schemas.UserCreate(
            email="testuser1@example.com",
            password=pwd_context.hash("1234"),
            type="regular"
        )
        crud.create_user(db, user=test_user)
    finally:
        db.close() 

    login_data = {
        "email": "testuser1@example.com",
        "password": "wrongpassword"
    }
    response = client.post("/login", json=login_data)

    assert response.status_code == 200
    assert response.json() == {"status": "failed"}
