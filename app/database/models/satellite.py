from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Satellite(Base):

    __tablename__ = "satellite_records"

    id = Column(Integer, primary_key=True, index=True)

    farm_id = Column(
        Integer,
        ForeignKey("farms.id"),
        nullable=False
    )

    capture_date = Column(DateTime)

    ndvi = Column(Float)

    evi = Column(Float)

    ndwi = Column(Float)

    surface_temperature = Column(Float)

    vegetation_health = Column(Float)

    farm = relationship(
        "Farm",
        back_populates="satellite_records"
    )

    def __repr__(self):
        return f"<Satellite {self.id}>"