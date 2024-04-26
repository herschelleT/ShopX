from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from typing import List
from db_manager import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(length=100), unique=True, index=True)
    hashed_password = Column(String(length=100))
    is_active = Column(Boolean, default=True)
    type = Column(String(length=10))
    orders : Mapped[List["Order"]] = relationship(back_populates="user")

class Phone(Base):
    __tablename__ = 'phones'

    id : Mapped[int] = mapped_column(primary_key=True)
    Brand = Column(String(length=20))
    Model = Column(String(length=20))

    RAM = Column(Integer)
    Storage = Column(Integer) # since for phones, ram and storage are both in GB
    Camera = Column(Integer) 

    
    Screen_Size = Column(Float)   # inches
    Camera = Column(Integer)  

    # battery_life = Column(Integer)
    Battery_Capacity = Column(Integer)
    Battery_Rating = Column(Enum("Average", "Good", "Excellent"))
    Price = Column(Float)
    # type = Column(String(length=50))
    Stock = Column(Integer)

class Order(Base):
    __tablename__ = 'orders'

    id : Mapped[int] = mapped_column(primary_key=True)
    Brand = Column(String(length=20))
    Model = Column(String(length=20))
    Price = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="orders")
