from sqlalchemy import Column, Integer, String, Text, DateTime

from app.database.database import Base


class AgentLog(Base):

    __tablename__ = "agent_logs"

    id = Column(Integer, primary_key=True, index=True)

    agent_name = Column(String(100))

    task_name = Column(String(150))

    status = Column(String(50))

    execution_time = Column(Integer)

    input_data = Column(Text)

    output_data = Column(Text)

    created_at = Column(DateTime)

    def __repr__(self):
        return f"<AgentLog {self.agent_name}>"