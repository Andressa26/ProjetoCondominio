from conexao import Conexao
from moradores import Moradores
from veiculos import Veiculos

m=Moradores()
v=Veiculos()
class MoradoresPossuemVeiculos(Conexao):
  def __init__(self):
    super().__init__()
    """Cria tabela"""
    self.main()
    self.namePk="idPosse"
  m.cpf="cpf"
  v.placa="placa"

  def main(self):
      sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS MoradoresPossuemVeiculos (
        idPosse INTEGER PRIMARY KEY,
        moradorFK TEXT NOT NULL,
        veiculoFK TEXT NOT NULL,
        FOREIGN KEY (moradorFK)
        REFERENCES Moradores (idMorador),
        FOREIGN KEY (veiculoFK)
        REFERENCES Veiculo (idVeiculo)
      ); """

      if self.conn is not None:
          # create veiculos table
          self.create_table(self.conn, sql_create_projects_table)
      else:
          print("Error! cannot create the database connection.")


  def selectKeyByCPF(self,coluna, tabela, cpf):
    cur= self.conn.cursor()
    cur.execute("SELECT "+coluna+" FROM "+tabela+" WHERE cpf=?", (cpf,))
    chave = cur.fetchall()
    return chave[0][0]
  
  def selectKeyByPlaca(self,coluna, tabela, placa):
    cur= self.conn.cursor()
    cur.execute("SELECT "+coluna+" FROM "+tabela+" WHERE placa=?", (placa,))
    chave = cur.fetchall()
    return chave[0][0]
  
  def create(self, dados):
      sql = ''' INSERT INTO MoradoresPossuemVeiculos(moradorFK, veiculoFK) VALUES(?,?) '''
      res = self.task(sql,dados)
      self.validateReturn(res, 'Cadastro')
      
  def dataCreate(self):
    cpf = int(input('Insira o CPF do morador: '))
    placa=input("Insira a placa do veículo: ")
    if self.checkExistence('Moradores', cpf, "cpf"):
      moradorFK = self.selectKeyByCPF("idMorador", "Moradores", cpf)
      veiculoFK= self.selectKeyByPlaca("idVeiculo","Veiculos",placa)
      self.create([moradorFK,veiculoFK])
    else:
      print("Morador ou veículo não cadastrados.")

  def validateReturn(self, response, action):
    if response == True:
      print(f'Ação de {action} de Posse de veículos realizada com sucesso!')
    else:
        print(response)

  def delete(self):
    print('Exclusão de posse de veículos')
    id = input('Insira o ID da posse de veículos que deseja excluir: ')
    if self.checkExistence('MoradoresPossuemVeiculos', id, self.namePk):
      sql = ''' DELETE FROM MoradoresPossuemVeiculos
      WHERE idPosse = ? '''
      res = self.task(sql, id)
      self.validateReturn(res, 'Exclusão')
    else:
      print(f'Posse de veículos com ID: {id} não foi encontrado para ser excluído.')

  def all(self):
    cur = self.conn.cursor()
    cur.execute("SELECT idPosse, m.cpf, v.placa FROM MoradoresPossuemVeiculos as p INNER JOIN Moradores as m ON m.idMorador=p.MoradorFK INNER JOIN Veiculos as v ON v.idVeiculo=p.VeiculoFK")
    rows = cur.fetchall()
    if type(rows) is list:
      if len(rows) <= 0:
        print('Não há posse de veículos  cadastradas!')
      else:
        print('Posses de veículos Cadastradas:')
        for i in range(len(rows)):
          print(f'ID: {rows[i][0]}')
          print(f'Morador: {rows[i][1]}')
          print(f'Veiculos: {rows[i][2]}')
          print('\n')    
    else:
      print('Ocorreu um erro ao consultar os dados.')
    