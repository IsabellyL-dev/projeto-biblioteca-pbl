from fastapi.testclient import TestClient
import sys
sys.path.append("src")
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200

def test_cadastrar_livro():
    r = client.post("/livros", json={"titulo": "Clean Code", "autor": "Robert Martin"})
    assert r.status_code == 200
    assert r.json()["titulo"] == "Clean Code"

def test_listar_livros():
    r = client.get("/livros")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_buscar_por_titulo():
    client.post("/livros", json={"titulo": "Python Fluente", "autor": "Ramalho"})
    r = client.get("/livros/buscar?titulo=python")
    assert r.status_code == 200

def test_alterar_status():
    client.post("/livros", json={"titulo": "Livro X", "autor": "Autor"})
    r = client.put("/livros/1/status?disponivel=false")
    assert r.status_code == 200

def test_remover_livro():
    r = client.delete("/livros/1")
    assert r.status_code == 200