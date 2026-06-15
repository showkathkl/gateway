from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.init import *

app = FastAPI()

#Enable Cors
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#Registers all routers
app.include_router(AuthenticationRouter)
app.include_router(ExpenseRouter)
for route in app.routes:
    print("ROUTE:", route.path)

@app.get("/")
def home():
    return "Started..."