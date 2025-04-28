import random
import requests

# variável do tipo constante pra guardar a url
URL_CRIAR_USUARIO = "https://desafiopython.jogajuntoinstituto.org/api/users/"

#Lista de nomes e sobrenomes
nomes = ["Lucas", "Maria", "João", "Ana", "Carlos", "Fernanda", "Paulo", "Julia", "Rafael", "Larissa"]
sobrenomes = ["Silva", "Oliveira", "Santos", "Pereira", "Costa", "Souza", "Almeida", "Rodrigues", "Martins", "Lima"]

# função parar criar um nome aleatório
def gerar_nome_usuario():
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    numero = random.randint(1, 999) 
    return f"{nome}{sobrenome}{numero}"

# função para criar um email aleatório
def gerar_email(nome_usuario):
    nome_usuario = nome_usuario.lower() #deixa tudo em minúsculo
    return f"{nome_usuario}@email.com"


# função para criar o usuário
def criar_usuario():
    try:

        nome_usuario = gerar_nome_usuario()
        email_usuario = gerar_email(nome_usuario)

        dados_usuario = {
        "username": nome_usuario,
        "email": email_usuario,
        "password": "123456786",
        "phone": "12345678901",
        "address": "123 Main St, City, Country",
        "cpf": "003.456.999-00"
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