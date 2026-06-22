from sqlalchemy import Column, Integer, String, Boolean
from src.database import Base


class LivroDB(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False, index=True)
    autor = Column(String, nullable=False)
    disponivel = Column(Boolean, default=True)