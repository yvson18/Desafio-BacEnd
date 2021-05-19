# Desafio BackEnd

A idéia do desafio era a de servir dados contidos em um arquivo dados.json para clientes através de uma API. A natureza dos dados era de proposições realizadas por entidades políticas. Foi requisitado que as rotas oferecidas pela a API fornecessem acesso aos seguintes recursos:

1.  Listar todas as proposições
2.  Listar proposições de um autor em específico
3.  Filtrar proposições por tipo

## Tecnologias usadas

Como possuo no momento mais familiaridade com python, optei por desenvolver a aplicação em tal linguagem. Utilizei para construção da API a framework FastAPI, devido a contato prévio com outros projetos.
É válido ressaltar que o arquivo "Requirements.txt" contém as libs usadas com suas respectivas versões.

## Algumas considerações no teste da API

Devido a problemas na exibição dos dados na listagem completa de todas as proposições do arquivo **Json**, resolvi criar um pequeno script para testar os recursos.