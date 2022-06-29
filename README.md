# b3-forecasting-tera

Repositório oficial do nosso projeto final da Tera. (transformar o README em capa do projeto depois)

## Configuração do ambiente de desenvolvimento

Para iniciar o ambiente de desenvolvimento, vamos subir o ambiente virtual do python **(venv)**, abra o repositório do projeto no VSCODE e abra um terminal para executar os comandos abaixo:

- Inicialiar o ambiente virtual `py -3 -m venv .venv`
- Ativar o venv `cd .\.venv\Scripts\activate`
- Agora podemos instalar as dependências de desenvolvimento `pip install -r requirements-dev.txt`
- Pronto, ambiente configurado para uso!

Caso necessite adicionar pacotes no projeto, não esqueça de atualizar as dependências de desenvolvimento, siga as etapas abaixo:

- `pip install <package>`
- `pip freeze > requirements.txt` para dependências do projeto
- `pip freeze > requirements-dev.txt` para dependências de desenvolvimento.
