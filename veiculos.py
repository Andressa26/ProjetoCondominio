from conexao import Conexao

class Veiculos(Conexao):
  def __init__(self):
    super().__init__()
    """Cria tabela"""
    self.main()
    self.namePk = "idVeiculo"

  def main(self):
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Veiculos (
      idVeiculo INTEGER PRIMARY KEY,
      placa TEXT UNIQUE NOT NULL,
      modelo TEXT NOT NULL,
      documento TEXT NOT NULL,
      cor TEXT NOT NULL,
      tipo TEXT NOT NULL
    ); """

    if self.conn is not None:
        # create veiculos table
        self.create_table(self.conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")

  def dataInput(self):
    placa = input('Insira a placa do veículo: ')
    modelo = input('Insira o modelo do veículo: ')
    documento = input('Insira o documento do veículo: ')
    cor = input('Insira a cor do veículo: ')
    tipo = input('Insira o tipo do veículo: ')
    return [placa, modelo, documento, cor, tipo]
    
  def dataCreate(self):
    print('Cadastro de Veículo')
    self.create(self.dataInput())

  def dataUpdate(self):
    print('Alteração de Veículo')
    id = int(input('Insira o ID do veículo que deseja alterar: '))
    if self.checkExistence('Veiculos', id, self.namePk):
      lista = self.dataInput()
      lista.append(id)
      self.update(lista)
    else:
      print(f'Veículo com ID: {id} não foi encontrado para ser alterado.')

  def validateReturn(self, response, action):
    if response == True:
      print(f'Ação de {action} do veículo realizada com sucesso!')
    else:
      print(response)

  def create(self, dados):
    sql = ''' INSERT INTO Veiculos(placa, modelo, documento, cor, tipo) VALUES(?,?,?,?,?) '''
    res = self.task(sql, dados)
    self.validateReturn(res, 'Cadastro')
  
  def update(self, dados):
    sql = ''' UPDATE Veiculos SET
    placa = ? , 
    modelo = ? ,
    documento = ? ,
    cor = ? , 
    tipo = ? WHERE idVeiculo = ? '''
    res = self.task(sql, dados)
    self.validateReturn(res, 'Alteração')

  def delete(self):
    print('Exclusão de Veículo')
    id = input('Insira o ID do veículo que deseja excluir: ')
    if self.checkExistence('Veiculos', id, self.namePk):
      sql = ''' DELETE FROM Veiculos WHERE idVeiculo = ? '''
      res = self.task(sql, id)
      self.validateReturn(res, 'Exclusão')
    else:
      print(f'Veículo com ID: {id} não foi encontrado para ser excluído.')
  
  def all(self):
    rows = self.select_all('Veiculos')
    if type(rows) is list:
      if len(rows) <= 0:
        print('Não há veículos cadastrados!')
      else:
        print('Veículos Cadastrados:')
        for i in range(len(rows)):
          print(f'ID: {rows[i][0]}')
          print(f'Placa: {rows[i][1]}')
          print(f'Modelo: {rows[i][2]}')
          print(f'Documento: {rows[i][3]}')
          print(f'Cor: {rows[i][4]}')
          print(f'Tipo: {rows[i][5]}')

          print('\n')  
    else:
      print('Ocorreu um erro ao consultar os dados.')
    
  def selectByPlaca(self):
    placa = input('Insira a placa do veículo para consultar: ')
    cur = self.conn.cursor()
    cur.execute("SELECT * FROM Veiculos WHERE placa=?", (placa,))
    rows = cur.fetchall()
    if type(rows) is list:
      if len(rows) <= 0:
        print(f'Não há veículos cadastrados com a placa: {placa}!')
      else:
        print('Veículo Encontrado::')
        print('ID\nPlaca\nModelo\nDocumento\nCor\nTipo\n')
        for i in range(len(rows)):
          print(f'ID: {rows[i][0]}')
          print(f'Placa: {rows[i][1]}')
          print(f'Modelo: {rows[i][2]}')
          print(f'Documento: {rows[i][3]}')
          print(f'Cor: {rows[i][4]}')
          print(f'Tipo: {rows[i][5]}')

          print('\n')   
    else:
      print('Ocorreu um erro ao consultar os dados.')