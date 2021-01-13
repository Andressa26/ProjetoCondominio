from conexao import Conexao

class Moradores(Conexao):
  
  def __init__(self):
    super().__init__()
    """Cria tabela"""
    self.main()
    self.namePk = "idMorador"
    self.nome="nome"

  def main(self):
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Moradores (
    idMorador INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    residenciaFK INTEGER NOT NULL,
    FOREIGN KEY(residenciaFK) 
    REFERENCES Residencias (idResidencia)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    ); """

      # create tables
    if self.conn is not None:
        # create Moradores table
        self.create_table(self.conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")


  def dataInputMoradores(self):
    nome =input("Digite o nome do morador:")
    cpf= input("Digite o CPF do morador:")
    residenciaFK= input("Digite a residencia do morador:")
    return [nome, cpf, residenciaFK]

  def dataCreateMoradores(self):
    print('Cadastro de Moradores')
    self.create(self.dataInputMoradores())

  def create(self, dados):
    sql = ''' INSERT INTO Moradores(nome, cpf, residenciaFK) VALUES(?,?,?) '''
    res = self.task(sql,dados)
    self.validateReturn(res, 'Cadastro')

  def validateReturn(self, response, action):
    if response == True:
      print(f'Ação de {action} do morador realizada com sucesso!')
    else:
      print(response)

  def dataUpdate(self):
    print('Alteração de Morador')
    id = int(input('Insira o ID do morador que deseja alterar: '))
    if self.checkExistence('Moradores', id, self.namePk):
      lista = self.dataInputMoradores()
      lista.append(id)
      self.update(lista)
    else:
      print(f'Morador com ID: {id} não foi encontrado para ser alterado.')

  def update(self, dados):
    sql = ''' UPDATE Moradores SET
    nome = ? , 
    cpf = ? ,
    residenciaFK = ? WHERE idMorador = ? '''
    res = self.task(sql,dados)
    self.validateReturn(res, 'Alteração')

  def delete(self):
    print('Exclusão de Morador')
    id = input('Insira o ID do morador que deseja excluir: ')
    if self.checkExistence('Moradores', id, self.namePk):
      sql = ''' DELETE FROM Moradores 
      WHERE idMorador = ? '''
      res = self.task(sql, id)
      self.validateReturn(res, 'Exclusão')
    else:
      print(f'Morador com ID: {id} não foi encontrado para ser excluído.')

  def selectNome(self):
    print('Pesquisa por nome:')
    nome= input('Insira o nome do morador: ')
    values=(nome,)
    if self.checkExistence('Moradores', nome, self.nome):
      m= self.conn.cursor()
      m.execute("SELECT * FROM Moradores WHERE nome = ?",values)
      resultado=m.fetchall()
      if len(resultado) <= 0:
        print('\nNão há moradores cadastrados com esse nome!')
      else:
        print(f'\nMoradores Cadastrados com nome {nome}:\n')
        for i in range(len(resultado)):
          print(f'ID: {resultado[i][0]}')
          print(f'Nome: {resultado[i][1]}')
          print(f'CPF: {resultado[i][2]}')
          print(f'Residência: {resultado[i][3]}')
          print('\n')   
          continue
      

  def allMoradores(self):
    rows = self.select_all('Moradores')
    if type(rows) is list:
      if len(rows) <= 0:
        print('Não há moradores cadastrados!')
      else:
        print(f'Moradores Cadastrados:\n')
        for i in range(len(rows)):
          print(f'ID: {rows[i][0]}')
          print(f'Nome: {rows[i][1]}')
          print(f'CPF: {rows[i][2]}')
          print(f'Residência: {rows[i][3]}')
          print('\n')    
     
    else:
      print('Ocorreu um erro ao consultar os dados.')





