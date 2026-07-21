from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Crop(Base):

    __tablename__ = "crops"

    id = Column(Integer, primary_key=True, index=True)

    farm_id = Column(
        Integer,
        ForeignKey("farms.id"),
        nullable=False
    )

    crop_name = Column(String(100), nullable=False)

    variety = Column(String(100))

    sowing_date = Column(Date)

    expected_harvest_date = Column(Date)

    season = Column(String(50))

    area = Column(Float)

    expected_yield = Column(Float)

    farm = relationship("Farm", back_populates="crops")

    def __repr__(self):
        return f"<Crop {self.crop_name}>"