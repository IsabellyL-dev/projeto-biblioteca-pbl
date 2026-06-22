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

## Banco de dados

O projeto usa PostgreSQL para persistência dos dados, rodando como serviço separado no Docker Compose. Os dados dos livros ficam salvos em um volume Docker, então continuam disponíveis mesmo depois de parar e subir os containers de novo (`docker compose down` sem a flag `-v`).

Variáveis de conexão ficam no `.env` (baseado no `.env.example`):

POSTGRES_USER=biblioteca_user
POSTGRES_PASSWORD=biblioteca_pass
POSTGRES_DB=biblioteca_db
DATABASE_URL=postgresql://biblioteca_user:biblioteca_pass@db:5432/biblioteca_db

O backend só inicia depois que o banco estiver pronto para aceitar conexões (`depends_on` com `condition: service_healthy` no `docker-compose.yml`).

## Rotas

| Método | Rota                    | Descrição               |
|--------|-------------------------|--------------------------|
| GET    | /livros                 | Lista todos os livros   |
| GET    | /livros/buscar?titulo=X | Busca por título        |
| POST   | /livros                 | Cadastra um livro       |
| PUT    | /livros/{id}/status     | Altera disponibilidade  |
| DELETE | /livros/{id}            | Remove um livro         |
| GET    | /health                 | Verifica a API          |

## Testes

Os testes automatizados usam um banco SQLite isolado, separado do PostgreSQL usado em produção, então não é preciso ter o Docker rodando para executá-los.

cd backend
pip install -r requirements.txt
python -m pytest tests/ -v

## Decisões técnicas

- FastAPI: framework moderno, simples e com documentação automática
- PostgreSQL: banco relacional para persistência real dos dados, com SQLAlchemy como ORM
- Docker: garante execução igual em qualquer máquina, com backend e banco como serviços separados na mesma rede
- GitHub Actions: pipeline gratuita integrada ao repositório