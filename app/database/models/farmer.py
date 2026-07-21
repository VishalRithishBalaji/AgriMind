from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.database.database import Base


class Farmer(Base):

    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    name = Column(String(150), nullable=False)

    phone = Column(String(20))

    village = Column(String(150))

    district = Column(String(150))

    state = Column(String(150))

    farm_size = Column(Float)

    user = relationship(
        "User",
        back_populates="farmers"
    )

    farms = relationship(
        "Farm",
        back_populates="farmer",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Farmer {self.name}>"