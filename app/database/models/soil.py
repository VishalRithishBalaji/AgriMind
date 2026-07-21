from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Soil(Base):

    __tablename__ = "soil_records"

    id = Column(Integer, primary_key=True, index=True)

    farm_id = Column(
        Integer,
        ForeignKey("farms.id"),
        nullable=False
    )

    recorded_at = Column(DateTime)

    ph = Column(Float)

    nitrogen = Column(Float)

    phosphorus = Column(Float)

    potassium = Column(Float)

    moisture = Column(Float)

    organic_carbon = Column(Float)

    soil_texture = Column(String(100))

    farm = relationship("Farm", back_populates="soil_records")

    def __repr__(self):
        return f"<Soil {self.id}>"