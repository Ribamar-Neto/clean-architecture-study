from sqlalchemy import Column, Integer, String

from src.settings.db.base import Base


class UsersInputSchema(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Users [id={self.id}, first_name={self.first_name}]"
