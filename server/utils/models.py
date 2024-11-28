from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Float, DateTime, func
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
    reviews : Mapped[List["Review"]] = relationship(back_populates="user")

class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    phone_id = Column(Integer, ForeignKey("phones.id"), nullable=True)
    laptop_id = Column(Integer, ForeignKey("laptops.id"), nullable=True)
    rating = Column(Float, nullable=False)
    text = Column(String, nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="reviews")
    phone: Mapped["Phone"] = relationship("Phone", back_populates="reviews", foreign_keys=[phone_id])
    laptop: Mapped["Laptop"] = relationship("Laptop", back_populates="reviews", foreign_keys=[laptop_id])

class Phone(Base):
    __tablename__ = 'phones'

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(length=20), nullable=False)
    model: Mapped[str] = mapped_column(String(length=20), nullable=False)
    ram: Mapped[int] = mapped_column(Integer, nullable=True)  # RAM in GB
    storage: Mapped[int] = mapped_column(Integer, nullable=True)  # Storage in GB
    camera: Mapped[int] = mapped_column(Integer, nullable=True)  # Camera in MP
    screen_size: Mapped[float] = mapped_column(Float, nullable=True)  # Screen size in inches
    battery_capacity: Mapped[int] = mapped_column(Integer, nullable=True)  # Battery capacity in mAh
    battery_rating: Mapped[str] = mapped_column(Enum("Average", "Good", "Excellent", name="rating_types"), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=True)  # Number of items in stock

    # Relationships
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="phone")
    orders: Mapped[List["Order"]] = relationship("Order", back_populates="phone")


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    Brand = Column(String(length=20))
    Model = Column(String(length=20))
    Price = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))
    phone_id = Column(Integer, ForeignKey("phones.id"))
    laptop_id = Column(Integer, ForeignKey("laptops.id"))
    timestamp = Column(DateTime, default=func.now())  # Timestamp for order creation

    user: Mapped["User"] = relationship(back_populates="orders")
    phone = relationship("Phone", back_populates="orders")

class Laptop(Base):
    __tablename__ = 'laptops'

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(length=50), nullable=False)
    model: Mapped[str] = mapped_column(String(length=50), nullable=False)
    processor: Mapped[str] = mapped_column(String(length=50), nullable=True)  # e.g., "Intel i7"
    ram: Mapped[int] = mapped_column(Integer, nullable=True)  # RAM in GB
    storage: Mapped[str] = mapped_column(String(length=50), nullable=True)  # e.g., "512GB SSD"
    screen_size: Mapped[float] = mapped_column(Float, nullable=True)  # Screen size in inches
    price: Mapped[float] = mapped_column(Float, nullable=False)

    # Relationship to reviews
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="laptop")

    def __repr__(self):
        return f"<Laptop(id={self.id}, brand={self.brand}, model={self.model}, price={self.price})>"
