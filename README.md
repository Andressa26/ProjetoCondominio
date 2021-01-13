# Linguagem de Programação II (LP2)
## Instituto Federal de São Paulo, Câmpus Bragança Paulista

## Projeto Semestral - Gerenciamento de Condomínio
**Integrantes:** 
- Andressa Rodrigues, BP3012701
- Bianca Vital, BP3012999
- Brendon Franco, BP3013227
- Matheus Munarão, BP3013251

A aplicação foi desenvolvida com a liguagem *Python* e banco de dados *SQLite* e trata-se de um sistema que possibilita efetuar a manutenção de moradores, visitantes, usuários, residências, veículos dos moradores e registro de movimentações de entrada e saída do condomínio. O sistema só pode ser acessado mediante autenticação, usando login e senha. Existem dois papéis de usuários para o sistema, como administrador que habilita acesso para todas as funções do sistema, incluindo cadastro, alteração, exclusão e consulta, e como não administrador, no caso denominamos de 'porteiro', o qual permite acesso mais restrito, podendo realizar consultas dos dados e apenas cadastrar movimentação de entrada e saída. 

## Funcionalidades do Programa
#### Para administradores:
    Manutenção de Veículos
    Manutenção de Moradores
    Manutenção de Usuários
    Manutenção de Residências
    Manutenção de Visitantes
    Cadastro e alteração de Movimentações
    Consulta, exclusão e cadastro de Posse de veículos
    Consulta de Usuário por nome, CPF ou função
    Consulta de Visitante por CPF
    Consulta de Veículo por placa
    Consulta de Movimentações em Aberto (sem data de saída)
    
#### Para não administradores:
    Registrar entrada
    Registrar saída
    Consultar Veículos
    Consultar Moradores
    Consultar Residências
    Consultar Visitantes
    Consultar Movimentações
    Consultar Movimentações em Aberto
    
Obs. por Movimentação considera-se as operações de Cadastro, Alteração, Consulta e Exclusão
## Paradigma Utilizado
O projeto foi desenvolvido usando o paradigma de programação orientada a objetos, afim de praticar os conceitos de classes, atributos e herança com a linguagem Python.

## Start
Para iniciar o programa, deve-se, primeiramente, baixar a pasta do projeto e executar o arquivo "main.py" que está na pasta. 