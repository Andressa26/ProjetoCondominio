from conexao import Conexao
from visitantes import Visitantes
from moradores import Moradores

m=Moradores()
vi=Visitantes()
class Movimentacoes(Conexao):
  
  def __init__(self):
    super().__init__()
    """Cria tabela"""
    self.main()
    self.namePk="idMovimentacao"
 
  m.cpf="cpf"
  vi.cpf="cpf"
  def main(self):
      sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Movimentacoes (
        idMovimentacao INTEGER PRIMARY KEY,
        descricao TEXT NOT NULL,
        data_entrada TEXT NOT NULL,
        data_saida TEXT NULL,
        moradorFK TEXT NULL,
        visitanteFK TEXT NULL,
        FOREIGN KEY (moradorFK)
        REFERENCES Moradores (idMorador),
        FOREIGN KEY (visitanteFK)
        REFERENCES Visitantes (idVisitante)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
      ); """

      if self.conn is not None:
          # create movimentacoes table
          self.create_table(self.conn, sql_create_projects_table)
      else:
          print("Error! cannot create the database connection.")

  def selectKeyByCPF(self,coluna, tabela, cpf):
    cur= self.conn.cursor()
    cur.execute("SELECT "+coluna+" FROM "+tabela+" WHERE cpf=?", (cpf,))
    chave = cur.fetchall()
    return chave[0][0]
  """
  def dataInputMorador(self):
    data_entrada=input("Digite a data de entrada: ")
    descricao =input("Digite a descrição: ")
    moradorFK=input("Digite o id do visitante: ")
    return [descricao, data_entrada, " ", moradorFK]

  def dataInputVisitante(self):
    data_entrada=input("Digite a data de entrada: ")
    descricao =input("Digite a descrição: ")
    visitanteFK=input("Digite o id do visitante: ")
    return [descricao, data_entrada, " ", visitanteFK]
    """
  
  def dataCreate(self):
    cpf = int(input('Insira o CPF: '))
    data_entrada=input("Insira a data de entrada: ")
    hora_entrada=input("Insira a hora da entrada: ")
    descricao =input("Insira a descrição: ")
    data_entrada= data_entrada +" "+ hora_entrada
    if self.checkExistence('Visitantes', cpf, "cpf"):
      print("É visitante")   
      visitanteFK = self.selectKeyByCPF("idVisitante", "Visitantes", cpf)
      self.createVisitante([descricao, data_entrada, " ", visitanteFK])
    elif self.checkExistence('Moradores', cpf, "cpf"):
      print("É morador")
      moradorFK = self.selectKeyByCPF("idMorador", "Moradores", cpf)
      self.createMorador([descricao, data_entrada, " ", moradorFK])
    else:
      print("CPF não cadastrado como visitante e nem como morador.")

  def createVisitante(self, dados):
    sql = ''' INSERT INTO Movimentacoes(descricao, data_entrada, data_saida, visitanteFK) VALUES(?,?,?,?) '''
    res = self.task(sql,dados)
    self.validateReturn(res, 'Cadastro')
 
  def createMorador(self, dados):
    sql = ''' INSERT INTO Movimentacoes(descricao, data_entrada, data_saida, moradorFK) VALUES(?,?,?,?) '''
    res = self.task(sql,dados)
    self.validateReturn(res, 'Cadastro')

  def validateReturn(self, response, action):
    if response == True:
      print(f'Ação de {action} do movimento realizada com sucesso!')
    else:
      print(response)
  
  def update(self):
    id=int(input('Insira o ID da movimentação que deseja resgistrar a saída: '))
    if self.checkExistence('Movimentacoes', id, self.namePk):
      data_saida= input("Insira a data da saída: ")
      hora=input("Insira a hora da saída: ")
      data_saida= data_saida +" "+ hora
      dados=[data_saida, id]
      sql = ''' UPDATE Movimentacoes SET
      data_saida = ? WHERE idMovimentacao = ? '''
      res = self.task(sql,dados)
      self.validateReturn(res, 'Alteração')
    else:
      print(f'Movimentação com ID: {id} não foi encontrado para ser alterado.')

  def all(self):
    rows = self.select_all('Movimentacoes')
    if type(rows) is list:
      if len(rows) <= 0:
        print('Não há movimentações cadastradas!')
      else:
        print('\nMovimentações Cadastradas:\n')
        for i in range(len(rows)):
          if rows[i][4] == "1":
            papel = "Morador"
          else:
            papel = "Visitante"
          print(f'ID: {rows[i][0]}')
          print(f'Descrição: {rows[i][1]}')
          print(f'Data entrada: {rows[i][2]}')
          print(f'Data saída: {rows[i][3]}')
          print(f'Visitante ou Morador? {papel}')
          print('\n')    
    else:
      print('Ocorreu um erro ao consultar os dados.')

  def selectMovAbertas(self):
    cur = self.conn.cursor()
    cur.execute("SELECT * FROM Movimentacoes WHERE data_saida=' '")
    rows = cur.fetchall()
    if type(rows) is list:
      if len(rows) <= 0:
        print('Não há movimentações em aberto!')
      else:
        for i in range(len(rows)):
          if rows[i][4] == "1":
            papel = "Morador"
          else:
            papel = "Visitante"
          print(f'ID: {rows[i][0]}')
          print(f'Descrição: {rows[i][1]}')
          print(f'Data entrada: {rows[i][2]}')
          print(f'Visitante ou Morador? {papel}')
          print('\n')   
    else:
      print('Ocorreu um erro ao executar a consulta.')
