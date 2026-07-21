from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database import crud
from app.database import schemas

router = APIRouter(
    prefix="/crops",
    tags=["Crops"]
)


# =====================================================
# CREATE CROP
# =====================================================

@router.post(
    "/",
    response_model=schemas.CropResponse,
    status_code=201
)
def create_crop(
    crop: schemas.CropCreate,
    db: Session = Depends(get_db)
):

    farm = crud.get_farm(db, crop.farm_id)

    if farm is None:
        raise HTTPException(
            status_code=404,
            detail="Farm not found."
        )

    return crud.create_crop(db, crop)


# =====================================================
# GET ALL CROPS
# =====================================================

@router.get(
    "/",
    response_model=List[schemas.CropResponse]
)
def get_crops(
    db: Session = Depends(get_db)
):

    return crud.get_crops(db)


# =====================================================
# GET CROP BY ID
# =====================================================

@router.get(
    "/{crop_id}",
    response_model=schemas.CropResponse
)
def get_crop(
    crop_id: int,
    db: Session = Depends(get_db)
):

    crop = crud.get_crop(db, crop_id)

    if crop is None:
        raise HTTPException(
            status_code=404,
            detail="Crop not found."
        )

    return crop


# =====================================================
# UPDATE CROP
# =====================================================

@router.put(
    "/{crop_id}",
    response_model=schemas.CropResponse
)
def update_crop(
    crop_id: int,
    crop: schemas.CropCreate,
    db: Session = Depends(get_db)
):

    updated_crop = crud.update_crop(
        db,
        crop_id,
        crop
    )

    if updated_crop is None:
        raise HTTPException(
            status_code=404,
            detail="Crop not found."
        )

    return updated_crop


# =====================================================
# DELETE CROP
# =====================================================

@router.delete("/{crop_id}")
def delete_crop(
    crop_id: int,
    db: Session = Depends(get_db)
):

    crop = crud.delete_crop(
        db,
        crop_id
    )

    if crop is None:
        raise HTTPException(
            status_code=404,
            detail="Crop not found."
        )

    return {
        "message": "Crop deleted successfully."
    }