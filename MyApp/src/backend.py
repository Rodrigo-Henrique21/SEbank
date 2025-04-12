import os
import re
import requests
import flet as ft
from supabase import create_client
from dotenv import load_dotenv
import bcrypt

load_dotenv()

url = os.getenv("url")
senha = os.getenv("senha")

supabase = create_client(url, senha)

def salvarCliente(dadosCompletos, callbackSucesso, callbackErro):
    try:
        senhaCriptografada = bcrypt.hashpw(dadosCompletos["senha"].encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        dadosParaBanco = {
            "nome": dadosCompletos["nome"],
            "cpf": dadosCompletos["cpf"],
            "email": dadosCompletos["email"],
            "telefone": dadosCompletos["telefone"],
            "cep": dadosCompletos.get("cep", ""),
            "rua": dadosCompletos["rua"],
            "numero": dadosCompletos.get("numero", ""),
            "bairro": dadosCompletos["bairro"],
            "cidade": dadosCompletos["cidade"],
            "uf": dadosCompletos["uf"],
            "usuario": dadosCompletos["usuario"],
            "senha": senhaCriptografada,
            "saldo": 0.0,
            "limiteCredito": 0.0,
            "limiteCreditoDiario": 0.0,
            "valorFatura": 0.0
        }

        response = supabase.table("dados").insert(dadosParaBanco).execute()

        if response.data:
            callbackSucesso()
        else:
            callbackErro("Falha ao inserir dados no banco")

    except Exception as erro:
        callbackErro(f"Erro no banco de dados: {str(erro)}")


def tirarErro(evento: ft.ControlEvent):
    evento.control.error_text = ""
    evento.control.update()

def verificarUsuarioNoSupabase(usuario, senha):
    try:
        resultado = supabase.table("dados").select("senha").eq("usuario", usuario).execute()

        if not resultado.data:
            return False

        senhaHash = resultado.data[0]["senha"]

        if bcrypt.checkpw(senha.encode("utf-8"), senhaHash.encode("utf-8")):
            return True
        else:
            return False

    except Exception as erro:
        print("Erro ao verificar usuário:", erro)
        return False

def verificarValoresInput(pagina, inputUsuario: ft.TextField, inputSenha: ft.TextField, sucessoCallback):
    if not inputUsuario.value and not inputSenha.value:
        inputUsuario.error_text = "Digite um usuário"
        inputSenha.error_text = "Digite uma senha"
    elif not inputUsuario.value:
        inputUsuario.error_text = "Digite um usuário"
        inputSenha.error_text = ""
    elif not inputSenha.value:
        inputUsuario.error_text = ""
        inputSenha.error_text = "Digite uma senha"
    else:
        usuarioExiste = verificarUsuarioNoSupabase(inputUsuario.value, inputSenha.value)
        if usuarioExiste:
            sucessoCallback()
        else:
            inputUsuario.error_text = "Usuário ou senha incorretos"
            inputSenha.error_text = "Usuário ou senha incorretos"
    pagina.update()

def formatarTelefone(evento: ft.ControlEvent):
    valorNumerico = ''.join(filter(str.isdigit, evento.control.value))[:11]
    telefoneFormatado = valorNumerico
    if len(valorNumerico) == 11:
        telefoneFormatado = f"({valorNumerico[:2]}) {valorNumerico[2:7]}-{valorNumerico[7:]}"
    elif len(valorNumerico) >= 7:
        telefoneFormatado = f"({valorNumerico[:2]}) {valorNumerico[2:6]}-{valorNumerico[6:]}"
    elif len(valorNumerico) >= 3:
        telefoneFormatado = f"({valorNumerico[:2]}) {valorNumerico[2:]}"
    evento.control.value = telefoneFormatado
    evento.page.update()

def validarEmail(evento: ft.ControlEvent):
    valorEmail = evento.control.value
    padraoValido = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if valorEmail and not re.match(padraoValido, valorEmail):
        evento.control.error_text = "E-mail inválido!"
    else:
        evento.control.error_text = ""
    evento.page.update()

def validarCpf(evento: ft.ControlEvent):
    valorCpf = ''.join(filter(str.isdigit, evento.control.value))[:11]
    evento.control.value = valorCpf
    if len(valorCpf) != 11 or len(set(valorCpf)) == 1:
        evento.control.error_text = "CPF inválido!"
    else:
        def calcularDv(parcial, pesos):
            soma = sum(int(digito) * peso for digito, peso in zip(parcial, pesos))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        if valorCpf[-2:] != calcularDv(valorCpf[:9], range(10, 1, -1)) + calcularDv(valorCpf[:10], range(11, 1, -1)):
            evento.control.error_text = "CPF inválido!"
        else:
            evento.control.error_text = ""
    evento.page.update()

def formatarNome(evento: ft.ControlEvent):
    evento.control.value = evento.control.value.title()
    evento.page.update()

def somenteNumero(evento: ft.ControlEvent):
    evento.control.value = ''.join(filter(str.isdigit, evento.control.value))
    evento.control.update()

def validarCep(evento: ft.ControlEvent, campoRua, campoBairro, campoCidade, campoUf):
    valorCep = ''.join(filter(str.isdigit, evento.control.value))[:8]
    evento.control.value = valorCep
    if len(valorCep) != 8:
        evento.control.error_text = "CEP incompleto"
        evento.page.update()
        return
    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{valorCep}/json/")
        dadosCep = resposta.json()
        if "erro" in dadosCep:
            evento.control.error_text = "CEP inválido"
        else:
            evento.control.error_text = ""
            campoRua.value = dadosCep.get("logradouro", "").upper()
            campoBairro.value = dadosCep.get("bairro", "").upper()
            campoCidade.value = dadosCep.get("localidade", "").upper()
            campoUf.value = dadosCep.get("uf", "").upper()
    except Exception:
        evento.control.error_text = "Erro ao buscar o CEP"
    evento.page.update()
