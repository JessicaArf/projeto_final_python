import requests

def criar_usuario():
    url_criar_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/"

    dados_usuario = {
        "username": "jessicateste",
        "email": "jessicateste@email.com",
        "password": "123456786",
        "phone": "12345678901",
        "address": "123 Main St, City, Country",
        "cpf": "003.456.999-00"
    }

    resposta = requests.post(url_criar_usuario, json=dados_usuario)

    print("Response criação do usuário: ")
    print(resposta.status_code)
    print(resposta.json())


criar_usuario() 