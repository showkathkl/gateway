from pydantic import BaseModel


class SignupSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str


class SigninSchema(BaseModel):
    username: str
    password: str


class UsersSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str
    role: int
    status: int


class ExpenseSchema(BaseModel):
    title: str
    description: str
    amount: float
    category: str
    date: str