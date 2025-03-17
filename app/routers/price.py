from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from app.models.model_price import OilSchema
from app.services.service_price import ExchangeService, OilService

router = APIRouter(
    prefix="/price",
    tags=["PRICE"],
    responses={404: {"message": "Not found"}}
)

exchange_service = ExchangeService()
oil_service = OilService()

@router.get("/exchange")
async def get_all():
    return exchange_service.get_all()

@router.post("/exchange/search")
async def get_search(name: str):
    return exchange_service.get_search(name)

@router.get("/oil")
async def get_all():
    return oil_service.get_all()

@router.post("/oil/search")
async def get_search(name: OilSchema):
    return oil_service.get_search(name)

@router.get("/gold")
async def get_all():
    return True