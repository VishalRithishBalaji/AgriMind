from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database import crud
from app.database import schemas

router = APIRouter(
    prefix="/farmers",
    tags=["Farmers"]
)


# =====================================================
# CREATE FARMER
# =====================================================

@router.post(
    "/",
    response_model=schemas.FarmerResponse,
    status_code=201
)
def create_farmer(
    farmer: schemas.FarmerCreate,
    db: Session = Depends(get_db)
):

    user = crud.get_user(db, farmer.user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    return crud.create_farmer(db, farmer)


# =====================================================
# GET ALL FARMERS
# =====================================================

@router.get(
    "/",
    response_model=List[schemas.FarmerResponse]
)
def get_farmers(
    db: Session = Depends(get_db)
):

    return crud.get_farmers(db)


# =====================================================
# GET FARMER BY ID
# =====================================================

@router.get(
    "/{farmer_id}",
    response_model=schemas.FarmerResponse
)
def get_farmer(
    farmer_id: int,
    db: Session = Depends(get_db)
):

    farmer = crud.get_farmer(db, farmer_id)

    if farmer is None:
        raise HTTPException(
            status_code=404,
            detail="Farmer not found."
        )

    return farmer


# =====================================================
# UPDATE FARMER
# =====================================================

@router.put(
    "/{farmer_id}",
    response_model=schemas.FarmerResponse
)
def update_farmer(
    farmer_id: int,
    farmer: schemas.FarmerCreate,
    db: Session = Depends(get_db)
):

    updated_farmer = crud.update_farmer(
        db,
        farmer_id,
        farmer
    )

    if updated_farmer is None:
        raise HTTPException(
            status_code=404,
            detail="Farmer not found."
        )

    return updated_farmer


# =====================================================
# DELETE FARMER
# =====================================================

@router.delete("/{farmer_id}")
def delete_farmer(
    farmer_id: int,
    db: Session = Depends(get_db)
):

    farmer = crud.delete_farmer(
        db,
        farmer_id
    )

    if farmer is None:
        raise HTTPException(
            status_code=404,
            detail="Farmer not found."
        )

    return {
        "message": "Farmer deleted successfully."
    }