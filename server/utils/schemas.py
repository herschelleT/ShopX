from pydantic import BaseModel
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from passlib.context import CryptContext
#AUTH
class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    username: str | None = None
    
class User(BaseModel):
    username: str
    email: str
    type: str

class PhoneCreate(BaseModel):
    Brand: str
    Model: str

    RAM:  int
    Storage: int # since for phones, ram and storage are both in GB

    Screen_Size: float   # inches
    Camera: int  

    # battery_life = Column(Integer)
    Battery_Capacity: int
    Battery_Rating: str
    Price: int
    # Main_camera: int #pixels,
    # type = Column(String(length=50))
    Stock: int
class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    type: str
class UserLogin(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
class OrderCreate(BaseModel):
    Brand: str
    Model: str
    Price: float
    user_id: int