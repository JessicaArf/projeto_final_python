import random
import requests

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
    nome_usuario = nome_usuario.lower()  # deixa tudo em minúsculo
    return f"{nome_usuario}@email.com"

# Função para criar um cpf aleatório
def gerar_cpf():
    numeros = [random.randint(0, 9) for _ in range(11)]  # Gera 11 dígitos aleatórios
    return f"{numeros[0]}{numeros[1]}{numeros[2]}.{numeros[3]}{numeros[4]}{numeros[5]}.{numeros[6]}{numeros[7]}{numeros[8]}-{numeros[9]}{numeros[10]}"

# Função para verificar se o usuário existe
def verificar_usuario_existente(nome_usuario):
    try:
        url = f"{URL_CRIAR_USUARIO}{nome_usuario}"
        resposta = requests.get(url)
        if resposta.ok:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print("Erro ao fazer requisição:", e)
        return None

# Função para criar o usuário
def criar_usuario():
    try:
        nome_usuario = gerar_nome_usuario()
        email_usuario = gerar_email(nome_usuario)
        cpf_usuario = gerar_cpf()

        # Verificar se o usuário existe
        usuario_existente = verificar_usuario_existente(nome_usuario)
        if usuario_existente:
            print(f"Usuário {nome_usuario} já existe. Gerando novo usuário...")
            # Volta o código para criar novo usuário como se fosse uma recursividade
            return criar_usuario()

        global dados_usuario
        dados_usuario = {
            "username": "Lucassasfsmeida5740",
            "email": "lucasdfsfaida5740@email.com",
            "password": "123456786",
            "phone": "12345678901",
            "address": "Rua Aparecida, Centro, São Paulo, SP",
            "cpf": "523.802.173-90"
        }

        resposta = requests.post(URL_CRIAR_USUARIO, json=dados_usuario)
        print("\n[Resposta da Criação do Usuário]")
        print(f"Status Code: {resposta.status_code}")
        if resposta.ok:
            print("Usuário criado com sucesso!")
            print(resposta.json())
        else:
            print("Falha ao criar usuário.")
            print(resposta.json())
    except requests.exceptions.RequestException as e:
        print("Erro ao fazer requisição:", e)

criar_usuario()

resposta_login = requests.post(URL_EFETUAR_LOGIN, json=dados_usuario)
print("\n[Resposta da execução do Login]")
print(f"Status Code: {resposta_login.status_code}")
print(f"ResponseBody: {resposta_login.request}")
