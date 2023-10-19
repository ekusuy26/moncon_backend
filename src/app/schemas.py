from typing import Union

from pydantic import BaseModel


class PaymentBase(BaseModel):
    date:str
    name:str
    amount:str


class PaymentCreate(PaymentBase):
    pass


class Payment(PaymentBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    payments: list[Payment] = []

    class Config:
        from_attributes = True
