<div align="center">
    <img align="center" alt="Teams-Logo" width=50% src="https://cdn.analyticsvidhya.com/wp-content/uploads/2019/07/rasa_chatbot.png">
    <h2>RasaBot - Test</h2>
</div>

### 1️⃣ Descrição
Este projeto tem a finalidade de ser um treino/teste da criação e manipulação de um chatbot utilizando Rasa.

Para isto utilizou-se a base de projeto criado com 
```bash
rasa init
```

Delimitei as intenções para apenas 3, sendo que o funcionamento de duas é mais percebida. A primeira de saudar e a segunda para a API. 

A primeira intenção se pode perceber interagindo com algumas mensagens, por exemplo:
```
- Bom dia
- Boa tarde
- Boa noite
- Ola
- Oi
- Tudo bem?
```

Já a intenção da API, utilizou-se a integração com a API do OpenAI (Chat GPT). Sua base de conversas é simples apenas para teste, pode-se seguir os seguintes exemplos de interação:
```
- Quantos pokemons existem até a sua data de atualização?
- O que são pokemons?
- Quantas temporadas existem?
- O que é um pokemon?
- O que é o pikachu?
- O que é o charizard?
- Me conte mais sobre pokemons
```

### 2️⃣ Demonstração
![preview](https://github.com/FeMarzani/RasaBot-Test/assets/107329291/38ea4402-0251-4183-83af-40a280822fce)


### 3️⃣ Como Utilizar
1. Instale o rasa em sua máquina utilizando o seguinte código abaixo:

    ```bash
    pip3 install rasa
    ```

2. Depois da instalação, clone este repositório.

3. Depois de clonar o repositório, navegue até a pasta ```app``` pelo terminal. 

4. Depois entrar na pasta app, crie um arquivo chamado ```.env``` e siga o modelo que se encontra no ```.env.example``` para adicionar as respectivas informações necessárias nas variáveis de ambiente para o projeto. Note que aqui foi utilizado as informações da api do chat gpt (open ai), portanto modifique a API_KEY para sua chave de API, o link adicione o link da api e o modelo utilize o id do modelo.  

5. Feito isso, utilize o comando abaixo para treinar o modelo a ser utilizado na interação:

    ```bash
    rasa train
    ```
    Este comando irá criar uma pasta chamada models e poderá ser percebido também uma pasta .rasa, onde estarão informações desse treinamento feito. 

6. Depois de treinar o modelo, basta executar. Para isso execute primeiro o código abaixo:

    ```bash
    rasa run actions
    ```

    E depois execute este código abaixo em outro terminal, sem fechar o terminal que estará executando o código do ```rasa run actions```, pois este comando é importante para permitir o funcionamento da classe que irá fazer a requisição na respectiva API. Portanto, execute este último código agora para interagir com o bot:

    ```bash
    rasa shell
    ```



