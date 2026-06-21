from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
from typing import List

from src.database import Base, engine, get_db
from src.models import LivroDB

app = FastAPI(title="Controle de Livros")

Base.metadata.create_all(bind=engine)


class Livro(BaseModel):
    titulo: str
    autor: str
    disponivel: bool = True

    class Config:
        from_attributes = True


class LivroResposta(Livro):
    id: int


@app.get("/livros", response_model=List[LivroResposta])
def listar_livros(db: Session = Depends(get_db)):
    return db.query(LivroDB).all()


@app.get("/livros/buscar")
def buscar_por_titulo(titulo: str, db: Session = Depends(get_db)):
    resultado = db.query(LivroDB).filter(
        func.lower(LivroDB.titulo).contains(titulo.lower())
    ).all()
    return resultado


@app.post("/livros", response_model=LivroResposta)
def cadastrar_livro(livro: Livro, db: Session = Depends(get_db)):
    novo = LivroDB(**livro.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@app.put("/livros/{id}/status")
def alterar_status(id: int, disponivel: bool, db: Session = Depends(get_db)):
    livro = db.query(LivroDB).filter(LivroDB.id == id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    livro.disponivel = disponivel
    db.commit()
    db.refresh(livro)
    return livro


@app.delete("/livros/{id}")
def remover_livro(id: int, db: Session = Depends(get_db)):
    livro = db.query(LivroDB).filter(LivroDB.id == id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    db.delete(livro)
    db.commit()
    return {"mensagem": "Livro removido com sucesso"}


@app.get("/health")
def health():
    return {"status": "ok"}