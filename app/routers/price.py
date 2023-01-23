from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from app.models.model_price import OilSchema
from app.services.service_price import ExchangeService, OilService

router = APIRouter(
    prefix="/price",
    tags=["PRICE"],
    responses={404: {"message": "Not found"}}
)

@router.get("/exchange")
async def get_all():
    return ExchangeService().get_all()

@router.post("/exchange/search")
async def get_search(name: str):
    return ExchangeService().get_search(name)

@router.get("/oil")
async def get_all():
    return OilService().get_all()

@router.post("/oil/search")
async def get_search(name: OilSchema):
    return OilService().get_search(name)

@router.get("/gold")
async def get_all():
    return True