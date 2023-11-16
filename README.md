# catalogo_veiculos_django

O banco de dados utilizado para o projeto foi o sqlite, o arquivo com o banco de dados já está disponível no projeto.
Para o funcionamento do projeto é necessário a instalação de algumas ferramentas:

```bash

pip install django djangorestframework

```
Para acessar a API Rest utilize o caminho "api/", o upload de imagens está sendo feito apenas pela api no caminho "api/carros".
Para deletar ou editar um carro basta usar o caminho "api/carros/(id do carro)".

Para acessar o admin do django utilize o caminho "admin/" (o usuário já criado é "admin" e a senha "123123"), onde é possível gerenciar todos os carros e usuários cadastrados.

Para fazer o login no site após clicar no botão "Entrar" na home page, você pode usar usuários cadastrados no admin do django, por exemplo, o "admin". Na Edição de Carros só é possível utilizar imagens que foram inseridas pela api (elas ficam armazenadas na pasta "media"). Ao fazer a edição de um carro após clicar no botão "Editar", é necessário enviar a imagem novamente.



