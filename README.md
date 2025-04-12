## 💰 SEbank – Aplicação Bancária com Python e Supabase

O **SEbank** é uma aplicação bancária fullstack desenvolvida com **Python** no backend e **Supabase** como backend-as-a-service (BaaS). A aplicação oferece funcionalidades básicas de uma conta bancária digital, com arquitetura organizada e escalável.

---

## 🚀 Funcionalidades

- Cadastro e login de usuários via Supabase Auth
- Visualização de saldo
- Saques
- Histórico de transações (em desenvolvimento)
- Estrutura modular com separação clara entre backend e frontend
- Gerenciamento de variáveis de ambiente via `.env`

---

## 🛠️ Tecnologias Utilizadas

### 🔙 Backend

- Python 3.9+
- FastAPI *(com base no `main.py` e `backend/backend.py`)*
- Supabase Python Client (`supabase-py`)
- Uvicorn (para execução local)
- Dotenv (para gerenciamento de configurações sensíveis)

### 🌐 Frontend

- Interface via script Python (`frontend/frontend.py`)
- Estrutura básica integrada ao backend

### 🗄️ Banco de Dados

- Supabase PostgreSQL
- Supabase Auth para autenticação
- Supabase Storage (não utilizado até o momento)

---

## 🧱 Estrutura do Projeto

```
banco-app/
│___ src
|
├───── backend/
|      ├── init.py
|      └── backend.py/
│
├───── frontend/
|      ├── init.py
|      └── frontend.py/
|
├── docs
├── assets
├── .env                      
├── requirements.txt
└── README.md

```

---

## 📦 Instalação e Execução

### 1️⃣ Clone o projeto

```bash
git clone https://github.com/seu-usuario/banco-app.git
cd banco-app
```

##  2️⃣ Backend
```
cd backend
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### Adicione suas chaves do Supabase no arquivo .env:

- SUPABASE_URL=https://xyzcompany.supabase.co
- SUPABASE_KEY=your-anon-or-service-role-key

## 3️⃣ Frontend

## 🧪 Exemplo de Uso da API (FastAPI)

### ➕ Cadastro

```
POST /register
{
  "email": "usuario@email.com",
  "password": "senha123"
}
```

## 🔐 Login

```
POST /login
{
  "email": "usuario@email.com",
  "password": "senha123"
}
```

## 💰 Consulta de saldo

### GET /saldo?user_id=abc123

### 🔐 Segurança
- ✅ Rotas protegidas com JWT

- ✅ Transações via HTTPS

- ✅ Autenticação delegada ao Supabase Auth

## 📋 TODO
 - Adicionar suporte a Pix ou QR Code para pagamentos

 - Criar dashboard com gráficos de gastos

 - Implementar notificações por e-mail

 - Realizar deploy automático (ex: Vercel + Railway)

## 👨‍💻 Contribuição
- Contribuições são bem-vindas!
- Abra uma issue ou envie um pull request com melhorias, correções ou sugestões.

## 📄 Licença
- Este projeto está sob a licença MIT.
- Consulte o arquivo LICENSE para mais informações.







