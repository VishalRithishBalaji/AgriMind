from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database import crud
from app.database import schemas

router = APIRouter(
    prefix="/farms",
    tags=["Farms"]
)


# =====================================================
# CREATE FARM
# =====================================================

@router.post(
    "/",
    response_model=schemas.FarmResponse,
    status_code=201
)
def create_farm(
    farm: schemas.FarmCreate,
    db: Session = Depends(get_db)
):

    farmer = crud.get_farmer(db, farm.farmer_id)

    if farmer is None:
        raise HTTPException(
            status_code=404,
            detail="Farmer not found."
        )

    return crud.create_farm(db, farm)


# =====================================================
# GET ALL FARMS
# =====================================================

@router.get(
    "/",
    response_model=List[schemas.FarmResponse]
)
def get_farms(
    db: Session = Depends(get_db)
):

    return crud.get_farms(db)


# =====================================================
# GET FARM BY ID
# =====================================================

@router.get(
    "/{farm_id}",
    response_model=schemas.FarmResponse
)
def get_farm(
    farm_id: int,
    db: Session = Depends(get_db)
):

    farm = crud.get_farm(db, farm_id)

    if farm is None:
        raise HTTPException(
            status_code=404,
            detail="Farm not found."
        )

    return farm


# =====================================================
# UPDATE FARM
# =====================================================

@router.put(
    "/{farm_id}",
    response_model=schemas.FarmResponse
)
def update_farm(
    farm_id: int,
    farm: schemas.FarmCreate,
    db: Session = Depends(get_db)
):

    updated_farm = crud.update_farm(
        db,
        farm_id,
        farm
    )

    if updated_farm is None:
        raise HTTPException(
            status_code=404,
            detail="Farm not found."
        )

    return updated_farm


# =====================================================
# DELETE FARM
# =====================================================

@router.delete("/{farm_id}")
def delete_farm(
    farm_id: int,
    db: Session = Depends(get_db)
):

    farm = crud.delete_farm(
        db,
        farm_id
    )

    if farm is None:
        raise HTTPException(
            status_code=404,
            detail="Farm not found."
        )

    return {
        "message": "Farm deleted successfully."
    }