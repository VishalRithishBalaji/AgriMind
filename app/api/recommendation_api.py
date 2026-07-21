from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database import crud
from app.database import schemas

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


# =====================================================
# CREATE RECOMMENDATION
# =====================================================

@router.post(
    "/",
    response_model=schemas.RecommendationResponse,
    status_code=201
)
def create_recommendation(
    recommendation: schemas.RecommendationCreate,
    db: Session = Depends(get_db)
):

    farm = crud.get_farm(db, recommendation.farm_id)

    if farm is None:
        raise HTTPException(
            status_code=404,
            detail="Farm not found."
        )

    return crud.create_recommendation(
        db,
        recommendation
    )


# =====================================================
# GET ALL RECOMMENDATIONS
# =====================================================

@router.get(
    "/",
    response_model=List[schemas.RecommendationResponse]
)
def get_recommendations(
    db: Session = Depends(get_db)
):

    return crud.get_recommendations(db)


# =====================================================
# GET RECOMMENDATION BY ID
# =====================================================

@router.get(
    "/{recommendation_id}",
    response_model=schemas.RecommendationResponse
)
def get_recommendation(
    recommendation_id: int,
    db: Session = Depends(get_db)
):

    recommendation = crud.get_recommendation(
        db,
        recommendation_id
    )

    if recommendation is None:
        raise HTTPException(
            status_code=404,
            detail="Recommendation not found."
        )

    return recommendation


# =====================================================
# UPDATE RECOMMENDATION
# =====================================================

@router.put(
    "/{recommendation_id}",
    response_model=schemas.RecommendationResponse
)
def update_recommendation(
    recommendation_id: int,
    recommendation: schemas.RecommendationCreate,
    db: Session = Depends(get_db)
):

    updated = crud.update_recommendation(
        db,
        recommendation_id,
        recommendation
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Recommendation not found."
        )

    return updated


# =====================================================
# DELETE RECOMMENDATION
# =====================================================

@router.delete("/{recommendation_id}")
def delete_recommendation(
    recommendation_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_recommendation(
        db,
        recommendation_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Recommendation not found."
        )

    return {
        "message": "Recommendation deleted successfully."
    }