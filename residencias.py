from conexao import Conexao

class Residencias(Conexao):
  def __init__(self):
    super().__init__()
    self.main()
    self.namePk="idResidencia"
    self.rua="rua"
    self.numero="numero"
    """Inicializa os atributos e cria tabela"""

  def main(self):
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Residencias (
      idResidencia INTEGER PRIMARY KEY,
      rua TEXT NOT NULL,
      numero INTEGER NOT NULL,
      cep TEXT NOT NULL,
      referencia_casa TEXT NULL
      ); """

    # create tables
    if self.conn is not None:
      # create Moradores table
      self.create_table(self.conn, sql_create_projects_table)
    else:
      print("Error! cannot create the database connection.")

  def dataInput(self):
    rua =input("Digite o nome da rua da residência: ")
    numero= input("Digite o numero da residência: ")
    cep= input("Digite o cep da residência: ")
    referencia_casa=input("Digite uma referência da residência: ")
    return [rua, numero, cep, referencia_casa]
  
  def dataCreate(self):
    print(f'Cadastro de Residência\n')
    self.create(self.dataInput())

  def create(self, dados):
    sql = ''' INSERT INTO Residencias(rua, numero, cep,referencia_casa) VALUES(?,?,?,?) '''
    res = self.task(sql,dados)
    self.validateReturn(res, 'Cadastro')

  def validateReturn(self, response, action):
    if response == True:
      print(f'Ação de {action} da residência realizada com sucesso!')
    else:
      print(response)
  
  def dataUpdate(self):
    print('Alteração de Residência')
    id = int(input('Insira o ID da residência que deseja alterar: '))
    if self.checkExistence('Residencias', id, self.namePk):
      lista = self.dataInput()
      lista.append(id)
      self.update(lista)
    else:
      print(f'Residencias com ID: {id} não foi encontrado para ser alterado.')

  def update(self, dados):
    sql = ''' UPDATE Residencias SET
    rua = ? , 
    numero = ? ,
    cep = ? ,
    referencia_casa= ? WHERE idResidencia = ? '''
    res = self.task(sql,dados)
    self.validateReturn(res, 'Alteração')

  def delete(self):
    print('Exclusão de Residências')
    id = input('Insira o ID do residências que deseja excluir: ')
    if self.checkExistence('Residencias', id, self.namePk):
      sql = ''' DELETE FROM Residencias
      WHERE idResidencia = ? '''
      res = self.task(sql, id)
      self.validateReturn(res, 'Exclusão')
    else:
      print(f'Residência com ID: {id} não foi encontrado para ser excluído.')
  
  def selectRua(self):
    print('Pesquisa por Logradouro e número:')
    rua= input('Insira o nome da rua da residência: ')
    numero= input('Insura o número da residência: ')
    values=(rua,numero,)
    if self.checkExistence('Residencias', rua, self.rua):
      if self.checkExistence('Residencias', numero, self.numero):
        vi= self.conn.cursor()
        vi.execute("SELECT * FROM Residencias WHERE rua = ? and numero=?",values)
        resultado=vi.fetchall()
        if len(resultado) <= 0:
          print('\nNão há residências cadastrados com esse CPF!')
        else:
          print(f'\nResidências Cadastrados com a rua {rua} e numero{numero}:\n')
          for i in range(len(resultado)):
            print(f'ID: {resultado[i][0]}')
            print(f'Rua: {resultado[i][1]}')
            print(f'Número: {resultado[i][2]}')
            print(f'CEP: {resultado[i][3]}')
            print(f'Referência casa: {resultado[i][4]}')

            print('\n')   
              
  
  def allResidencia(self):
    rows = self.select_all('Residencias')
    if type(rows) is list:
      if len(rows) <= 0:
        print('Não há residencias cadastrados cadastrados!')
      else:
        print('Residências Cadastrados:')
        for i in range(len(rows)):
          print(f'ID: {rows[i][0]}')
          print(f'Rua: {rows[i][1]}')
          print(f'Número: {rows[i][2]}')
          print(f'CEP: {rows[i][3]}')
          print(f'Referência casa: {rows[i][4]}')

          print('\n')   
          continue     
    else:
      print('Ocorreu um erro ao consultar os dados.')