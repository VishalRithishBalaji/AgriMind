from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class DecisionHistory(Base):

    __tablename__ = "decision_history"

    id = Column(Integer, primary_key=True, index=True)

    farm_id = Column(
        Integer,
        ForeignKey("farms.id"),
        nullable=False
    )

    decision_type = Column(String(100), nullable=False)

    input_summary = Column(Text)

    final_decision = Column(Text)

    confidence = Column(Integer)

    created_at = Column(DateTime)

    farm = relationship(
        "Farm",
        back_populates="decision_histories"
    )

    def __repr__(self):
        return f"<DecisionHistory {self.id}>"