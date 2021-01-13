from conexao import Conexao
from getpass import getpass

class Usuarios(Conexao):
  def __init__(self):
    super().__init__()
    """Cria tabela"""
    self.main()
    self.namePk = "idUsuario"

  def main(self):
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Usuarios (
      idUsuario INTEGER PRIMARY KEY,
      nome TEXT NOT NULL,
      cpf TEXT UNIQUE NOT NULL,
      login TEXT UNIQUE NOT NULL,
      senha TEXT NOT NULL,
      admin TEXT NOT NULL
    ); """

    if self.conn is not None:
        # create usuarios table
        self.create_table(self.conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")

  def dataInput(self):
    nome = input('Insira o nome: ')
    cpf = input('Insira o CPF: ')
    login = input('Insira um username para login: ')
    senha = getpass('Insira uma senha: ')
    admin = input('O usuário será administrador? Insira 1 para sim ou 0 para não : ')
    return [nome, cpf, login, senha, admin]
    
  def dataCreate(self):
    print('Cadastro de Usuário')
    self.create(self.dataInput())

  def dataUpdate(self):
    print('Alteração de Usuário')
    id = int(input('Insira o ID do Usuário que deseja alterar: '))
    if self.checkExistence('Usuarios', id, self.namePk):
      lista = self.dataInput()
      lista.append(id)
      self.update(lista)
    else:
      print(f'Usuário com ID: {id} não foi encontrado para ser alterado.')

  def validateReturn(self, response, action):
    if response == True:
      print(f'Ação de {action} do usuário realizada com sucesso!')
    else:
      print(response)

  def create(self, dados):
    sql = ''' INSERT INTO Usuarios(nome, cpf, login, senha, admin) VALUES(?,?,?,?,?) '''
    res = self.task(sql, dados)
    self.validateReturn(res, 'Cadastro')

  def update(self, dados):
    sql = ''' UPDATE Usuarios SET
    nome = ? , 
    cpf = ? ,
    login = ? ,
    senha = ? , 
    admin = ? WHERE idUsuario = ? '''
    res = self.task(sql, dados)
    self.validateReturn(res, 'Alteração')

  def delete(self):
    print('Exclusão de Usuário')
    id = input('Insira o ID do usuário que deseja excluir: ')
    if self.checkExistence('Usuarios', id, self.namePk):
      sql = ''' DELETE FROM Usuarios WHERE idUsuario = ? '''
      res = self.task(sql, id)
      self.validateReturn(res, 'Exclusão')
    else:
      print(f'Usuário com ID: {id} não foi encontrado para ser excluído.')
  
  def all(self):
    rows = self.select_all('Usuarios')
    if type(rows) is list:
      if len(rows) <= 0:
        print('Não há usuários cadastrados!')
      else:
        print('\nUsuários Cadastrados:\n')
        for i in range(len(rows)):
          if rows[i][5] == "1":
            admin = "Sim"
          else:
            admin="Não"
          print(f'ID: {rows[i][0]}')
          print(f'Nome: {rows[i][1]}')
          print(f'CPF: {rows[i][2]}')
          print(f'Login: {rows[i][3]}')
          print(f'Admin? {admin}')
          print('\n')
    else:
      print('Ocorreu um erro ao consultar os dados.')

  def authenticate(self, login, senha): 
    cur = self.conn.cursor()
    cur.execute("SELECT nome, senha, admin FROM Usuarios WHERE login=?", (login,))
    row = cur.fetchall()
    response = ''
    if len(row) == 0:
      response = 'Login inválido!'
    else:
      if row[0][1] != senha:
        response = 'Senha incorreta!'
      else:
        response = row[0][2]
    return response   
    
  def loginInput(self):
    res = ""
    while res != "0" and res != "1":
      login = input('\nInsira seu login: ')
      senha = getpass('Insira sua senha: ')
      if len(login) <= 0 or len(senha) <= 0:
        print('É necessário informail login e senha.')
      else:
        res = self.authenticate(login, senha)
      if res != "0" and res != "1":
        print(res)
    return res

  def selectBase(self, coluna, valor):
    cur = self.conn.cursor()
    cur.execute("SELECT idUsuario, nome, cpf, login,admin FROM Usuarios WHERE "+coluna+"=?", (valor,))
    rows = cur.fetchall()
    if type(rows) is list:
      if len(rows) <= 0:
        print(f'Não há usuários cadastrados com o {coluna}: {valor}!')
      else:
        print(f'Usuários Cadastrados com o {coluna}: {valor}')
        for i in range(len(rows)):
          if rows[i][4] == "1":
            admin = "Sim"
          else:
            admin="Não"
          print(f'ID: {rows[i][0]}')
          print(f'Nome: {rows[i][1]}')
          print(f'CPF: {rows[i][2]}')
          print(f'Login: {rows[i][3]}')
          print(f'Admin? {admin}')
          print('\n')
    else:
      print('Ocorreu um erro ao consultar os dados.')

  def selectByName(self):
    nome = input('\nInsira o nome do usuário: ')
    self.selectBase('nome', nome)

  def selectByCPF(self):
    cpf = input('\nInsira o CPF do usuário: ')
    self.selectBase('cpf', cpf)

  def selectByFunc(self):
    print('Selecione uma opção para consulta:')
    print('1. Exibir administradores')
    print('2. Exibir porteiros')
    valor = input('Entre com uma opção: ')
    if valor == "1":
      admin = valor
    elif valor == "2":
      admin = "0"
    else:
      print('Opção inválida.')
      return 0
    cur = self.conn.cursor()
    cur.execute("SELECT idUsuario, nome, cpf, login FROM Usuarios WHERE admin=?", (admin,))
    rows = cur.fetchall()
    if valor == "1":
      funcao = "administradores"
    else:
      funcao = "porteiros"
    if type(rows) is list:
      if len(rows) <= 0:
          print(f'Não há {funcao} cadastrados!')
      else:
        print(f'{funcao.title()} cadastrados:')
        for i in range(len(rows)):
          print(f'ID: {rows[i][0]}')
          print(f'Nome: {rows[i][1]}')
          print(f'CPF: {rows[i][2]}')
          print(f'Login: {rows[i][3]}')
          print('\n')
    else:
      print('Ocorreu um erro ao consultar os dados.')
    
