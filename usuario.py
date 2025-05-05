import os
import random
import requests
import json
from cpf_generator import CPF
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Variável do tipo constante pra guardar a url
URL_CRIAR_USUARIO = "https://desafiopython.jogajuntoinstituto.org/api/users/"
URL_EFETUAR_LOGIN = "https://desafiopython.jogajuntoinstituto.org/api/users/login/"

# Lista de nomes e sobrenomes
nomes = ["Lucas", "Maria", "João", "Ana", "Carlos", "Fernanda", "Paulo", "Julia", "Rafael", "Larissa"]
sobrenomes = ["Silva", "Oliveira", "Santos", "Pereira", "Costa", "Souza", "Almeida", "Rodrigues", "Martins", "Lima"]

# Função para criar um nome aleatório
def gerar_nome_usuario():
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    numero = random.randint(1, 9999)
    return f"{nome}{sobrenome}{numero}"

# Função para criar um email aleatório
def gerar_email(nome_usuario):
    nome_usuario = nome_usuario.lower()  #deixa tudo em minúsculo
    return f"{nome_usuario}@email.com"

# Função para criar um cpf aleatório
def gerar_cpf():
    return CPF.generate()

# Função para criar o usuário
def criar_usuario():
    try:
        nome_usuario = gerar_nome_usuario()
        email_usuario = gerar_email(nome_usuario)
        cpf_usuario = gerar_cpf()
        senha = os.getenv("USER_PASSWORD")
        telefone_usuario = "12345678901"
        endereco_usuario = "Rua Aparecida, Centro, São Paulo, SP"

        dados_usuario = {
            "username": nome_usuario,
            "email": email_usuario,
            "password": senha,
            "phone":telefone_usuario,
            "address": endereco_usuario,
            "cpf": cpf_usuario
        }

        resposta = requests.post(URL_CRIAR_USUARIO, json=dados_usuario)
        print("\n[Resposta da Criação do Usuário]")
        print(f"Status Code: {resposta.status_code}")

        if resposta.ok:
            print("Usuário criado com sucesso!")
            print(resposta.json())
            return dados_usuario 

        else:
            print("Falha ao criar usuário.")
            print(resposta.json())

    except requests.exceptions.RequestException as e:
        print("Erro ao fazer requisição:", e)
        

def realizar_login(dados_usuario):
    try:
        resposta_login = requests.post(URL_EFETUAR_LOGIN, json=dados_usuario)
        print("\n[Resposta do Login]")
        print(f"Status Code: {resposta_login.status_code}")
        print(resposta_login.json())

        if resposta_login.ok:
            print("Login efetuado com sucesso!")
            with open("login_response.json", "w") as arquivo:
                json.dump(resposta_login.json(), arquivo, indent=4)
        else:
            print("Falha ao efetuar login.")

    except requests.exceptions.RequestException as e:
        print("Erro ao fazer requisição de login:", e)


# --- Execução principal ---
dados = criar_usuario()
if dados:
    realizar_login(dados)
