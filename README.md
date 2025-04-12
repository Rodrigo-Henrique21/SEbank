# 💰 Aplicação Bancária com Python, Supabase e Frontend

Este projeto é uma **aplicação bancária fullstack** desenvolvida com **Python no backend**, **Supabase** como backend-as-a-service (BaaS), e um **frontend interativo** para a interface do usuário.

---

## 🚀 Funcionalidades

- ✅ Cadastro e login de usuários com autenticação via **Supabase**
- ✅ Visualização de **saldo e extrato bancário**
- ✅ **Transferência** de valores entre contas
- ✅ **Depósito** e **saque**
- ✅ **Histórico de transações**
- ✅ Integração segura entre **frontend**, **backend** e **Supabase**

---

## 🛠️ Tecnologias Utilizadas

### 🔙 Backend

- Python  
- FastAPI *(ou Flask)*  
- Supabase Python Client (`supabase-py`)  
- JWT para autenticação segura *(opcional)*

### 🌐 Frontend

- HTML, CSS e JavaScript *(ou React)*  
- Axios para chamadas à API  
- Bootstrap ou TailwindCSS para estilização

### 🗄️ Banco de Dados

- Supabase PostgreSQL  
- Supabase Auth *(autenticação)*  
- Supabase Storage *(opcional, para arquivos)*

---

## 🧱 Estrutura do Projeto

```
banco-app/
│_____ src
|
├───── backend/
|      ├── main.py               # Entrada da API (FastAPI)
|      ├── services/
|      ├── models/
|      └── supabase_client.py    # Conexão com o Supabase
│
├───── frontend/
|      ├── index.html
|      ├── login.html
|      ├── dashboard.html
|      └── js/
|          └── scripts.js
│
├── .env                      # Variáveis de ambiente
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


### Abra frontend/index.html no navegador
### Ou utilize ferramentas como:

* Live Server (VS Code)

* React App

* Vite

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







