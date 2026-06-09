from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Controle de Livros")

livros = []
contador_id = 1

class Livro(BaseModel):
    titulo: str
    autor: str
    disponivel: bool = True

class LivroResposta(Livro):
    id: int

@app.get("/livros", response_model=List[LivroResposta])
def listar_livros():
    return livros

@app.get("/livros/buscar")
def buscar_por_titulo(titulo: str):
    resultado = [l for l in livros if titulo.lower() in l["titulo"].lower()]
    return resultado

@app.post("/livros", response_model=LivroResposta)
def cadastrar_livro(livro: Livro):
    global contador_id
    novo = {"id": contador_id, **livro.model_dump()}
    livros.append(novo)
    contador_id += 1
    return novo

@app.put("/livros/{id}/status")
def alterar_status(id: int, disponivel: bool):
    for livro in livros:
        if livro["id"] == id:
            livro["disponivel"] = disponivel
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.delete("/livros/{id}")
def remover_livro(id: int):
    global livros
    livros = [l for l in livros if l["id"] != id]
    return {"mensagem": "Livro removido com sucesso"}

@app.get("/health")
def health():
    return {"status": "ok"}