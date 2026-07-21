from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Weather(Base):

    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True, index=True)

    farm_id = Column(
        Integer,
        ForeignKey("farms.id"),
        nullable=False
    )

    recorded_at = Column(DateTime)

    temperature = Column(Float)

    humidity = Column(Float)

    rainfall = Column(Float)

    wind_speed = Column(Float)

    pressure = Column(Float)

    farm = relationship("Farm", back_populates="weather_records")

    def __repr__(self):
        return f"<Weather {self.id}>"