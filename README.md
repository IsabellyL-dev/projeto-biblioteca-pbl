# projeto-biblioteca-pbl
Projeto sistema de biblioteca

# 📚 Controle de Livros — PBL DevOps

Sistema de controle de livros para biblioteca acadêmica.

## Como executar

git clone <url-do-repositorio>
cd projeto-biblioteca-pbl
cp .env.example .env
docker compose up --build

API disponível em: http://localhost:8000
Documentação automática: http://localhost:8000/docs

## Rotas

| Método | Rota                    | Descrição               |
|--------|-------------------------|-------------------------|
| GET    | /livros                 | Lista todos os livros   |
| GET    | /livros/buscar?titulo=X | Busca por título        |
| POST   | /livros                 | Cadastra um livro       |
| PUT    | /livros/{id}/status     | Altera disponibilidade  |
| DELETE | /livros/{id}            | Remove um livro         |
| GET    | /health                 | Verifica a API          |

## Testes

pip install -r backend/requirements.txt
pytest backend/tests/

## Decisões técnicas

- FastAPI: framework moderno, simples e com documentação automática
- Docker: garante execução igual em qualquer máquina
- GitHub Actions: pipeline gratuita integrada ao repositório