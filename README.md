# 🐍 Projeto Final Python 

![alt text](image.png)

Este é o projeto final do módulo de Python do curso de QA avançado do Instituto Joga Junto. O objetivo é criar uma aplicação que interaja com uma API fornecida para realizar três funcionalidades principais.

## 🚀Funcionalidades

### ✅  1. Criação de Usuário

A primeira funcionalidade do projeto consiste em criar um novo usuário utilizando a API. Para isso, utilizaremos o seguinte endpoint:

[https://desafiopython.jogajuntoinstituto.org/api/users/](https://desafiopython.jogajuntoinstituto.org/api/users/)

- O projeto deve enviar uma requisição **POST** com os dados do novo usuário no formato **JSON**.
- Exemplos de dados a serem enviados:
```json
{
  "username": "novo_usuario",
  "email": "novo@email.com",
  "password": "senha123",
  "phone": "1199999999",
  "address": "Rua Exemplo, 123",
  "cpf": "123.456.789-00"
}  
```  
### 🔐2. Login do Usuário

Após a criação do usuário, a aplicação deve realizar o login com o usuário recém-criado. Isso será feito utilizando o seguinte endpoint:

[https://desafiopython.jogajuntoinstituto.org/api/users/login](https://desafiopython.jogajuntoinstituto.org/api/users/login)

- A requisição de login deve ser do tipo **POST** e conter as credenciais do usuário no formato **JSON** no corpo da requisição.
- Os dados a serem enviados no corpo da requisição de login são:
```json
    {
       "username": "novo_usuario",
       "email": "novo@email.com",
       "password": "senha123",
       "phone": "1199999999",
       "address": "Rua Exemplo, 123",
       "cpf": "123.456.789-00"
    }
```
- A requisição de login deve conter as credenciais do usuário.
- Se o login for bem-sucedido, a API responderá com um token de autenticação.

**💾3. Salvar Resposta JSON:**

* O projeto deve salvar o JSON recebido como resposta das interações de login com a API.

- A resposta JSON pode conter informações como:

    - `refresh`: Um token de atualização (refresh token).

    - `access`: Um token de acesso (access token) que será usado para autenticar outras requisições.

    - `user`: Informações sobre o usuário autenticado, como `username`.

## 🛠️Como Executar o Projeto

1. **Clone o repositório:**
    ```
    git clone https://github.com/JessicaArf/projeto_final_python.git
    cd projeto_final_python
    ```

2. **Crie um arquivo .env na raiz do projeto e adicione a variável de senha:**
   ```
    USER_PASSWORD=senha
   ```

3. **Instale as dependências:**
    ```
   pip install requests cpf-generator python-dotenv
    ```

4. **Execute o script:**
    ```
    python usuario.py
    ```

## 📂 Arquivos Gerados

`login_response.json`: contém a resposta da API após o login, incluindo os tokens e os dados do usuário.

## 📌 Observações

- O CPF é gerado automaticamente com a biblioteca cpf-generator.

- Os dados do usuário (nome, email, etc.) são gerados aleatoriamente.

- Requisições HTTP são feitas com a biblioteca requests.

- Variáveis sensíveis, como a senha, devem ser configuradas no .env.