# No Scaries

O No Scaries é uma plataforma desenvolvida para automatizar a análise e classificação de e-mails recebidos, utilizando tecnologias avançadas de Processamento de Linguagem Natural (NLP) e Inteligência Artificial (IA). O objetivo é facilitar a triagem, priorização e resposta de e-mails, trazendo mais agilidade e eficiência para empresas e pessoas que recebem grande volume de mensagens diariamente.

## Funcionalidades

* Envio de e-mails para análise via upload (.pdf ou .txt) ou texto manual.
* Classificação automática dos e-mails (Produtivo/Improdutivo).
* Sugestão automática de respostas para e-mails produtivos.
* Histórico de e-mails analisados (acesso restrito a cada usuário).
* Interface amigável e responsiva (Bootstrap).
* Autenticação de usuários.

## Pré-requisitos

* [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/install/) instalados na sua máquina.
* Um arquivo `.env` com as variáveis de ambiente necessárias. Exemplo básico:

```
DEBUG=0
ALLOWED_HOSTS=127.0.0.1,localhost
SECRET_KEY=CHANGE_ME
# CSRF_TRUSTED_ORIGINS=

DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=CHANGE_ME
POSTGRES_USER=CHANGE_ME
POSTGRES_PASSWORD=CHANGE_ME
POSTGRES_HOST=django_psql
POSTGRES_PORT=5432

HUGGINGFACE_API_KEY=CHANGE_ME
```

> **Obs:** Verifique se todas as variáveis de ambiente necessárias para Django, banco de dados e APIs externas estão no seu `.env`.

## Como rodar o projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/noscary.git
   cd noscary
   ```

2. **Crie e configure seu arquivo `.env`** conforme o exemplo acima.

3. **Suba os containers com Docker Compose:**

   ```bash
   docker compose up --build
   ```

   O comando irá construir as imagens e iniciar os containers do backend (Django) e do banco de dados (PostgreSQL).

4. **Acesse a aplicação:**

   O sistema estará disponível em [http://localhost:3000](http://localhost:3000) (ou porta configurada no seu docker-compose).

5. **(Opcional) Executar migrações e criar superusuário:**

   Caso necessário, execute os comandos abaixo em outro terminal:

   ```bash
   docker compose exec django_app python manage.py migrate
   docker compose exec django_app python manage.py createsuperuser
   ```

## Tecnologias

* Python 3.x + Django
* PostgreSQL
* Docker
* Bootstrap 5
* Font Awesome

## Observações

* Apenas usuários autenticados podem acessar o histórico dos seus próprios e-mails.
* Não esqueça de configurar corretamente sua variável SECRET\_KEY.
* O sistema usa NLP/IA para classificação dos e-mails. Configure as variáveis de API/external se necessário.

---
