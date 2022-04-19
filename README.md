# Python Base PCA
## Projeto de Exemplo

Esse projeto é utilizado como base para estudos de Clean Architecture

## Origem

Esse projeto foi concebido para solucionar um problema onde um projeto era alterado era gerado vários pipelines.
Da forma como o projeto foi estruturado é possível integrar vários pontos de entrada sem que se conheçam, como por exemplo API RestFull, SOAP, Consumers entre outros de forma com que uma parte do projeto é compartilhada, sendo essa o diretório [core]

## Tech

- [Python]
- [FastAPI]
- [Psycopg2]

## Observações

Para a execução do projeto e a evolução dele é necessário que o conteúdo do requirements.txt do [core] seja copiado para cada ponto de entrada da aplicação afim de que o ambiente que irá subir possua todas as dependências.

## TODO: Testes

A estrutura foi pensada de forma que irá evoluir para que seja possível realizar testes onde camadas não sejam necessárias, como por exemplo a camada de negócio poderá ser testada sem que a camada de banco de dados esteja conectada.

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [core]: <https://github.com/felippetadeu/operacional/tree/master/core>
   [Python]: <https://www.python.org/>
   [FastAPI]: <https://fastapi.tiangolo.com/>
   [Psycopg2]: <https://pypi.org/project/psycopg2/>