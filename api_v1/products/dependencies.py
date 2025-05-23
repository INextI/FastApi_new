from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Product
from . import crud

async def product_by_id(
        product_id: Annotated[int, Path], 
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
    ) -> Product:
    product =  await crud.get_product(product_id= product_id, session= session)
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found!",
    )
