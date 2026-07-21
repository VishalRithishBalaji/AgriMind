from sqlalchemy import Column, Integer, String, Float, DateTime

from app.database.database import Base


class Market(Base):

    __tablename__ = "market_prices"

    id = Column(Integer, primary_key=True, index=True)

    crop_name = Column(String(100), nullable=False)

    market_name = Column(String(150))

    district = Column(String(100))

    state = Column(String(100))

    minimum_price = Column(Float)

    maximum_price = Column(Float)

    modal_price = Column(Float)

    recorded_at = Column(DateTime)

    def __repr__(self):
        return f"<Market {self.crop_name}>"