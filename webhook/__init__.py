from fastapi import FastAPI
from .webhook_router_fastapi import webhook_router

app = FastAPI()

app.include_router(webhook_router)