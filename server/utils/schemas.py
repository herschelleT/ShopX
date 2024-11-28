from pydantic import BaseModel
from typing import Optional

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
    brand: str
    model: str
    ram: Optional[int] = None
    storage: Optional[int] = None
    camera: Optional[int] = None
    screen_size: Optional[float] = None
    battery_capacity: Optional[int] = None
    battery_rating: Optional[str] = None
    price: float
    stock: Optional[int] = None

class PhoneResponse(BaseModel):
    id: int
    brand: str
    model: str
    ram: Optional[int]
    storage: Optional[int]
    camera: Optional[int]
    screen_size: Optional[float]
    battery_capacity: Optional[int]
    battery_rating: Optional[str]
    price: float
    stock: Optional[int]
    average_rating: Optional[float] = None
    order_count: int = 0

    class Config:
        orm_mode = True

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
    Price: float = None
    user_id: int
    phone_id: int = None  # Optional, in case an order is for a phone
    laptop_id: int = None  # Optional, in case an order is for a laptop

class PhoneFilter(BaseModel):
    min_ram: Optional[int] = None  # Minimum RAM in GB
    max_ram: Optional[int] = None  # Maximum RAM in GB
    min_storage: Optional[int] = None  # Minimum storage in GB
    max_storage: Optional[int] = None  # Maximum storage in GB
    min_camera: Optional[int] = None  # Minimum camera in MP
    max_camera: Optional[int] = None  # Maximum camera in MP
    min_screen_size: Optional[float] = None  # Minimum screen size in inches
    max_screen_size: Optional[float] = None  # Maximum screen size in inches
    min_battery_capacity: Optional[int] = None  # Minimum battery capacity in mAh
    max_battery_capacity: Optional[int] = None  # Maximum battery capacity in mAh
    battery_rating: Optional[str] = None  # Battery rating as "Average", "Good", or "Excellent"
    min_price: Optional[float] = None  # Minimum price
    max_price: Optional[float] = None  # Maximum price

class ReviewCreate(BaseModel):
    user_id: int
    phone_id: Optional[int] = None
    laptop_id: Optional[int] = None
    rating: float
    text: Optional[str] = None

class ReviewWithUserEmail(BaseModel):
    id: int
    content: str
    rating: float
    phone_id: Optional[int] = None
    laptop_id: Optional[int] = None
    user_email: str

    class Config:
        orm_mode = True
