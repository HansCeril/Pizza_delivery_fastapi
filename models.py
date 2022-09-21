from enum import unique
from database import Base
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, Text
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders=relationship('Order', back_populates='user')


    def __str__(self) -> str:
        return f"<user {self.username}"

class Order(Base):

    ORDER_STATUS=(
        ('PENDING', 'pending'),
        ('TRANSIT', 'transit'),
        ('DELIVERED', 'delivered')
    )

    PIZZA_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRALARGE', 'extralarge')
    )
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status=Column(ChoiceType(choices=ORDER_STATUS), default="PENDING")
    pizza_size=Column(ChoiceType(choices=PIZZA_SIZES), default='MEDIUM')
    user_id=Column(Integer, ForeignKey('user.id'))
    user=relationship('User', back_populates='order')

    def __str__(self) -> str:
        return f"<order {self.id}"



