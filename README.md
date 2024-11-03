# Aplicação de CRUD de Livros com Flask

## Descrição

Esta é uma aplicação web desenvolvida em Flask que permite o gerenciamento de uma biblioteca de livros. Os usuários podem cadastrar novos livros, fazer upload de capas, visualizar a lista de livros cadastrados, editar informações de livros existentes e removê-los. A aplicação também inclui funcionalidades de autenticação de usuários, garantindo que apenas usuários autorizados possam fazer alterações. Além disso, implementa um sistema de cache para melhorar o desempenho e criptografa as senhas dos usuários para garantir a segurança.

## Funcionalidades

- **Cadastro de Livros**: Os usuários podem cadastrar livros, incluindo título, autor, ano de publicação, descrição e uma imagem de capa.
- **Edição e Exclusão**: Possibilidade de editar as informações de livros cadastrados ou excluí-los.
- **Autenticação de Usuários**: Sistema de login que permite apenas usuários autenticados acessarem as funcionalidades de CRUD.
- **Criptografia de Senhas**: As senhas dos usuários são armazenadas de forma segura utilizando hashing.
- **Tratamento de Cache**: Implementação de cache para melhorar o desempenho da aplicação ao armazenar temporariamente dados frequentemente acessados.

## Tecnologias Utilizadas

- **Flask**: Microframework para desenvolvimento web em Python.
- **Flask-SQLAlchemy**: ORM para gerenciar o banco de dados.
- **Flask-Login**: Para gerenciar autenticação de usuários.
- **Flask-Caching**: Para implementar o tratamento de cache.
- **Werkzeug**: Para criptografia de senhas.
- **HTML/CSS**: Para a construção da interface do usuário.

## Requisitos

Antes de executar a aplicação, certifique-se de que você tem os seguintes pré-requisitos instalados:

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
   pip install -r requirements.txt

Edite as configurações de banco de dados no arquivo config.py se necessário.
Execute a aplicação:
  flask run

Uso
Acesse a aplicação no seu navegador em http://127.0.0.1:5000.
Registre-se ou faça login com um usuário existente.
Utilize as funcionalidades de cadastro, edição e exclusão de livros.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a MIT License.

### Personalizações

Sinta-se à vontade para ajustar o texto, adicionar instruções específicas sobre como usar a aplicação ou modificar as seções conforme necessário. Se você tiver informações adicionais, como um link para a documentação ou exemplos de uso, também pode incluí-las no README.
