from fastapi import APIRouter, HTTPException, status, Depends
from . import crud
from core.models import db_helper
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from .dependencies import product_by_id

router = APIRouter(tags=["Products"])

@router.get("/", response_model=list[Product])
async def get_products(session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    return await crud.get_products(session=session)

@router.post("/", response_model= Product, status_code=status.HTTP_201_CREATED)
async def create_product(product_in: ProductCreate, session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    return await crud.create_product(session=session, product_in=product_in)

@router.get("/{product_id}/", response_model= Product)
async def get_product(
    product: Product = Depends(product_by_id)
    ):
    return product


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    product: Product = Depends(product_by_id), 
    ) -> None:
    await crud.delete_product(product=product, session= session)


@router.put("/{product_id}/", response_model= Product)
async def put_product(
        product_update: ProductUpdate,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        product: Product = Depends(product_by_id),
    ):
    return await crud.update_product(session=session, product=product, product_update=product_update)


@router.patch("/{product_id}/", response_model= Product)
async def put_product(
        product_update: ProductUpdatePartial,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        product: Product = Depends(product_by_id),
    ):
    return await crud.update_product(session=session, product=product, product_update=product_update, partial= True)