from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Recommendation(Base):

    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)

    farm_id = Column(
        Integer,
        ForeignKey("farms.id"),
        nullable=False
    )

    recommendation_type = Column(String(100))

    recommendation = Column(Text)

    confidence = Column(Integer)

    generated_at = Column(DateTime)

    agent_name = Column(String(100))

    farm = relationship(
        "Farm",
        back_populates="recommendations"
    )

    def __repr__(self):
        return f"<Recommendation {self.id}>"