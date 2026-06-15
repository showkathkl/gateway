from fastapi import APIRouter, Header
from models.schemas import ExpenseSchema
import httpx
import os
from dotenv import load_dotenv
print("EXPENSE CONTROLLER LOADED")
load_dotenv()

router = APIRouter(prefix="/expense")

NODE_URL = os.getenv("NODE_URL")


@router.post("/addexpense")
async def addExpense(data: ExpenseSchema, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{NODE_URL}/expense/addexpense",
            json=data.model_dump(),
            headers={"Token": Token}
        )
    return response.json()


@router.get("/getallexpenses/{PAGE}/{SIZE}")
async def getAllExpenses(PAGE: int, SIZE: int, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{NODE_URL}/expense/getallexpenses/{PAGE}/{SIZE}",
            headers={"Token": Token}
        )
    return response.json()


@router.get("/getexpense/{ID}")
async def getExpense(ID: str, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{NODE_URL}/expense/getexpense/{ID}",
            headers={"Token": Token}
        )
    return response.json()


@router.put("/updateexpense/{ID}")
async def updateExpense(ID: str, data: ExpenseSchema, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{NODE_URL}/expense/updateexpense/{ID}",
            json=data.model_dump(),
            headers={"Token": Token}
        )
    return response.json()


@router.delete("/deleteexpense/{ID}")
async def deleteExpense(ID: str, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{NODE_URL}/expense/deleteexpense/{ID}",
            headers={"Token": Token}
        )
    return response.json()
@router.get("/searchexpense/{KEY}")
async def searchExpense(KEY: str, Token: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{NODE_URL}/expense/searchexpense/{KEY}",
            headers={"Token": Token}
        )

    return response.json()