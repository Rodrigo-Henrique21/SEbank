import os
from supabase import create_client
from dotenv import load_dotenv

# Inicializa o Supabase
def conectar_supabase():
    load_dotenv()
    url = os.getenv("url")
    senha = os.getenv("senha")

    if not url or not senha:
        raise ValueError("Variáveis de ambiente não definidas.")
    
    return create_client(url, senha)

# Função para sacar valor de um CPF
def realizar_saque(cpf: str, valor_saque: float):
    supabase = conectar_supabase()

    try:
        # Busca o usuário pelo CPF
        response = supabase.table("dados").select("*").eq("cpf", cpf).single().execute()
        usuario = response.data

        if not usuario:
            print("Usuário não encontrado.")
            return False

        saldo_atual = usuario["saldo"]

        if saldo_atual < valor_saque:
            print("Saldo insuficiente.")
            return False

        novo_saldo = saldo_atual - valor_saque

        # Atualiza o saldo no banco
        update_response = (
            supabase.table("dados")
            .update({"saldo": novo_saldo})
            .eq("cpf", cpf)
            .execute()
        )

        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso. Novo saldo: R$ {novo_saldo:.2f}")
        return True

    except Exception as e:
        print(f"Erro ao realizar saque: {e}")
        return False
