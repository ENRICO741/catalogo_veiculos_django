# catalogo_veiculos_django

O banco de dados utulizado para o projeto foi o sqlite, o arquivo com o banco de dados já está disponivel no projeto.
Para o funcionamento do projeto é nescessario a instalação de algumas ferramentas:

```bash

pip install django djangorestframework

```
Para acessar a API Rest utilize o caminho "api/", o upload de imagens está sendo feito apenas pela api no caminho "api/carros".
Para deletar ou editar um carro basta usar o caminho "api/carros/(id do carro)".

Para acessar o admin do django utilize o caminho "admin/", o usuario já criado é "admin" e a senha "123123", lá é gerenciar todos carros e usuarios cadastrados.

Para fazer o login no site após clicar no botão "Entrar" na home page, você pode usar usuarios cadastrados no admin do django, como por exemplo o "admin". Na Ediação de Carros só é possivel utilizar imagens que foram inseridas pela api (elas ficam armazenadas na pasta "media"). Ao fazer a edição de um carro após clicar no botão "Editar", é nescessario enviar a imagem novamente.



