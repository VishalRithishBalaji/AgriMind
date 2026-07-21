from sqlalchemy import Column, Integer, String, Text, DateTime

from app.database.database import Base


class MemoryStore(Base):

    __tablename__ = "memory_store"

    id = Column(Integer, primary_key=True, index=True)

    memory_type = Column(String(100))

    memory_key = Column(String(200), unique=True)

    memory_value = Column(Text)

    embedding_model = Column(String(100))

    source = Column(String(100))

    created_at = Column(DateTime)

    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<MemoryStore {self.memory_key}>"