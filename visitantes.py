from conexao import Conexao

class Visitantes(Conexao):
  def __init__(self):
    super().__init__()
    """Cria tabela"""
    self.main()
    self.namePk = "idVisitante"
    self.cpf="cpf"

  def main(self):
      sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Visitantes (
        idVisitante INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        placa TEXT NOT NULL
      ); """

      if self.conn is not None:
          # create visitantes table
          self.create_table(self.conn, sql_create_projects_table)
      else:
          print("Error! cannot create the database connection.")

  def dataInput(self):
    nome =input("Digite o nome do visitante:")
    cpf= input("Digite o CPF do visitante:")
    placa= input("Digite a placa do veiculo:")
    return [nome, cpf, placa]
  
  def dataCreate(self):
    print(f'Cadastro de Visitantes\n')
    self.create(self.dataInput())

  def create(self, dados):
    sql = ''' INSERT INTO Visitantes(nome, cpf, placa) VALUES(?,?,?) '''
    res = self.task(sql,dados)
    self.validateReturn(res, 'Cadastro')

  def validateReturn(self, response, action):
    if response == True:
      print(f'Ação de {action} do visitante realizada com sucesso!')
    else:
      print(response)

  def dataUpdate(self):
    print('Alteração de Visitante')
    id = int(input('Insira o ID do visitante que deseja alterar: '))
    if self.checkExistence('Visitantes', id, self.namePk):
      lista = self.dataInput()
      lista.append(id)
      self.update(lista)
    else:
      print(f'Visitante com ID: {id} não foi encontrado para ser alterado.')

  def update(self, dados):
    sql = ''' UPDATE Visitantes SET
    nome = ? , 
    cpf = ? ,
    placa = ? WHERE idVisitante = ? '''
    res = self.task(sql,dados)
    self.validateReturn(res, 'Alteração')

  def delete(self):
    print('Exclusão de Visitantes')
    id = input('Insira o ID do visitante que deseja excluir: ')
    if self.checkExistence('Visitantes', id, self.namePk):
      sql = ''' DELETE FROM Visitantes 
      WHERE idVisitante = ? '''
      res = self.task(sql, id)
      self.validateReturn(res, 'Exclusão')
    else:
      print(f'Visitante com ID: {id} não foi encontrado para ser excluído.')
  
  def selectCPF(self):
    print('Pesquisa por CPF:')
    cpf= input('Insira o cpf do morador: ')
    values=(cpf,)
    if self.checkExistence('Visitantes', cpf, self.cpf):
      vi= self.conn.cursor()
      vi.execute("SELECT * FROM Visitantes WHERE cpf = ?",values)
      resultado=vi.fetchall()
      if len(resultado) <= 0:
        print('\nNão há visitantes cadastrados com esse CPF!')
      else:
        print(f'\nVisitantes Cadastrados com CPF {cpf}:\n')
        for i in range(len(resultado)):
          print(f'ID: {resultado[i][0]}')
          print(f'Nome: {resultado[i][1]}')
          print(f'CPF: {resultado[i][2]}')
          print(f'Placa: {resultado[i][3]}')

          print('\n')   

  def allVisitantes(self):
    rows = self.select_all('Visitantes')
    if type(rows) is list:
      if len(rows) <= 0:
        print('Não há visitantes cadastrados cadastrados!')
      else:
        print('Visitantes Cadastrados:')
        for i in range(len(rows)):
          print(f'ID: {rows[i][0]}')
          print(f'Nome: {rows[i][1]}')
          print(f'CPF: {rows[i][2]}')
          print(f'Placa: {rows[i][3]}')
          continue     
    else:
      print('Ocorreu um erro ao consultar os dados.')
      
visitante = Visitantes()
visitante.select_all('Visitantes')