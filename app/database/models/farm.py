from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Farm(Base):

    __tablename__ = "farms"

    id = Column(Integer, primary_key=True, index=True)

    farmer_id = Column(
        Integer,
        ForeignKey("farmers.id")
    )

    farm_name = Column(String(150))

    latitude = Column(Float)

    longitude = Column(Float)

    total_area = Column(Float)

    soil_type = Column(String(100))

    irrigation_type = Column(String(100))

    farmer = relationship(
        "Farmer",
        back_populates="farms"
    )

    crops = relationship(
        "Crop",
        back_populates="farm",
        cascade="all, delete-orphan"
    )

    weather_records = relationship(
        "Weather",
        back_populates="farm",
        cascade="all, delete-orphan"
    )

    soil_records = relationship(
        "Soil",
        back_populates="farm",
        cascade="all, delete-orphan"
    )

    satellite_records = relationship(
        "Satellite",
        back_populates="farm",
        cascade="all, delete-orphan"
    )

    recommendations = relationship(
        "Recommendation",
        back_populates="farm",
        cascade="all, delete-orphan"
    )

    decision_histories = relationship(
        "DecisionHistory",
        back_populates="farm",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Farm {self.farm_name}>"