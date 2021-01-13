from veiculos import Veiculos
from moradores import Moradores
from visitantes import Visitantes
from usuarios import Usuarios
from residencias import Residencias
from movimentacoes import Movimentacoes
from posseVeiculos import MoradoresPossuemVeiculos

m = Moradores()
u = Usuarios()
v = Veiculos()
r = Residencias()
mov = Movimentacoes()
vi = Visitantes()
p=MoradoresPossuemVeiculos()

def menu_veiculos():
  title = "Manutenção de Veículos"
  print("\n")
  print('-' * len(title))
  print(title)
  print('-' * len(title))
  print('')
  print('Selecione uma opção para Veículos. Digite 0 para sair.')
  print('')
  print('1. Exibir todos os veículos.')
  print('2. Cadastrar um veículo.')
  print('3. Alterar um veículo.')
  print('4. Excluir um veículo.')
  print('5. Pesquisar um veículo pela placa.')
  choice1 = int(input("Entre com o número da opção: "))
  print('')
  return choice1

def menu_moradores():
  title = "Manutenção de moradores"
  print("\n")
  print('-' * len(title))
  print(title)
  print('-' * len(title))
  print('')
  print('Selecione uma opção para moradores.Digite 0 para sair.')
  print('')
  print('1. Exibir todos os moradores.')
  print('2. Pesquisar morador por nome')
  print('3. Cadastrar um morador.')
  print('4. Alterar um morador.')
  print('5. Excluir um morador.')
  print('6. Voltar ao menu anterior')
  choice2 = int(input("Entre com o número da opção: "))
  print('')
  return choice2

def menu_usuarios():
  title = "Manutenção de Usuários"
  print("\n")
  print('-' * len(title))
  print(title)
  print('-' * len(title))
  print('')
  print('Selecione uma opção para Usuários. Digite 0 para sair.')
  print('')
  print('1. Exibir todos os usuários.')
  print('2. Cadastrar um usuário.')
  print('3. Alterar um usuário.')
  print('4. Excluir um usuário.')
  print('5. Consultar usuário por nome.')
  print('6. Consultar usuário por CPF.')
  print('7. Consultar usuário por função.')
  choice4 = int(input("Entre com o número da opção: "))
  print('')
  return choice4

def menu_residencias():
  title = "Manutenção de residências"
  print("\n")
  print('-' * len(title))
  print(title)
  print('-' * len(title))
  print('')
  print('Selecione uma opção para residências.Digite 0 para sair.')
  print('')
  print('1. Exibir todos os residências.')
  print('2. Pesquisar residências por Lougradoro e número')
  print('3. Cadastrar uma residência.')
  print('4. Alterar uma residências.')
  print('5. Excluir uma residência.')
  print('6. Voltar ao menu anterior')
  choice3 = int(input("Entre com o número da opção: "))
  print('')
  return choice3

def menu_visitantes():
  title = "Manutenção de visitantes"
  print("\n")
  print('-' * len(title))
  print(title)
  print('-' * len(title))
  print('')
  print('Selecione uma opção para visitantes.Digite 0 para sair.')
  print('')
  print('1. Exibir todos os visitantes.')
  print('2. Pesquisar visitante por CPF')
  print('3. Cadastrar um visitante.')
  print('4. Alterar um visitante.')
  print('5. Excluir um visitante.')
  print('6. Voltar ao menu anterior')
  choice5 = int(input("Entre com o número da opção: "))
  print('')
  return choice5

def menu_posseVeiculos():
  title = "Manutenção de posse de veículos"
  print("\n")
  print('-' * len(title))
  print(title)
  print('-' * len(title))
  print('')
  print('Selecione uma opção posse de veículos.Digite 0 para sair.')
  print('')
  print('1. Exibir veículos e seus respectivos donos.')
  print('2. Cadastrar uma posse de veículo.')
  print('3. Excluir uma posse de veículo.')
  print('4. Voltar ao menu anterior')
  choice6 = int(input("Entre com o número da opção: "))
  print('')
  return choice6

def menu_movimentacao():
  title = "Manutenção de movimentações"
  print("\n")
  print('-' * len(title))
  print(title)
  print('-' * len(title))
  print('')
  print('Selecione uma opção para movimentações.Digite 0 para sair.')
  print('')
  print('1. Exibir todas as movimentações.')
  print('2. Exibir movimentações abertas')
  print('3. Cadastrar nova movimentação.')
  print('4. Registrar saída')
  print('5. Voltar ao menu anterior.')
  choice7 = int(input("Entre com o número da opção: "))
  print('')
  return choice7

def menu_admin():
  title = "Menu principal"
  print("\n")
  print('-' * len(title))
  print(title)
  print('-' * len(title))
  print('')
  print('Selecione uma opção. Digite 0 para sair.')
  print('')
  print('1. Veículos')
  print('2. Moradores')
  print('3. Usuários')
  print('4. Residências')
  print('5. Visitantes')
  print('6. Posse de veículos')
  print('7. Movimentações')
  choice = int(input("Entre com o número da opção: "))
  print('')
  return choice

def menu_porteiro():
  title = "Menu principal"
  print("\n")
  print('-' * len(title))
  print(title)
  print('-' * len(title))
  print('')
  print('Selecione uma opção. Digite 0 para sair.')
  print('')
  print('1. Registrar entrada')
  print('2. Registrar saída')
  print('3. Consultar Veículos')
  print('4. Consultar Moradores')
  print('5. Consultar Residências')
  print('6. Consultar Visitantes')
  print('7. Consultar Movimentações')
  print('8. Consultar Movimentações em Aberto')
  choice = int(input("Entre com o número da opção: "))
  print('')
  return choice

def opcoes_porteiro():
  choice = menu_porteiro()
  while choice != 0:
    if choice == 1:
      mov.dataCreate()
    elif choice == 2:
      mov.update()
    elif choice == 3:
      v.all()
    elif choice == 4:
      m.allMoradores()
    elif choice == 5:
      r.allResidencia()
    elif choice == 6:
      vi.allVisitantes()
    elif choice == 7:
      mov.all() 
    elif choice == 8:
      mov.selectMovAbertas() 
    else:
      print("Opção inválida.")
    choice = menu_porteiro()

def opcoes_admin():
  choice = menu_admin()
  while choice != 0:
    if choice == 1:
      choice1 = menu_veiculos()
      while choice1 != 0:
        if choice1 == 1:
          v.all()
        elif choice1 == 2:
          v.dataCreate()
        elif choice1 == 3:
          v.dataUpdate()
        elif choice1 == 4:
          v.delete()
        elif choice1 == 5:
          v.selectByPlaca()
        elif choice1 == 0:
          break
        else:
          print("Opção inválida.")
        choice1 = menu_veiculos()

    #Moradores
    elif choice == 2:
      choice2 = menu_moradores()
      while choice2 != 0:       
        if choice2 == 1:
          m.allMoradores()
        elif choice2 == 2:
          m.selectNome()
        elif choice2 == 3:
          m.dataCreateMoradores()
        elif choice2==4:
          m.dataUpdate()
        elif choice2==5:
          m.delete()
        elif choice2 == 0 or choice2==6:
          break
        else:
          print("Opção inválida.")
        choice2=menu_moradores()

    #Usuários
    elif choice == 3:
      choice3 = menu_usuarios()
      while choice3 != 0:
        if choice3 == 1:
          u.all()
        elif choice3 == 2:
          u.dataCreate()
        elif choice3 == 3:
          u.dataUpdate()
        elif choice3 == 4:
          u.delete()
        elif choice3 == 5:
          u.selectByName()
        elif choice3 == 6:
          u.selectByCPF()
        elif choice3 == 7:
          u.selectByFunc()
        elif choice3 == 0:
          break
        else:
          print("Opção inválida.")
        choice3 = menu_usuarios()
    
    #Residencias
    elif choice==4:
      choice3= menu_residencias()
      while choice3!=0:
        if choice3==1:
          r.allResidencia()
          choice3=menu_residencias()
        elif choice3==2:
          r.selectRua()
          choice3=menu_residencias()
        elif choice3==3:
          r.dataCreate()
          choice3=menu_residencias()
        elif choice3==4:
          r.dataUpdate()
          choice3=menu_residencias()
        elif choice3==5:
          r.delete()
          choice3=menu_residencias()
        elif choice3==0 or choice3==6:
          break
        else:
          print("Opção inválida.")
        choice3=menu_residencias()

    #VISITANTES
    elif choice==5:
      choice5=menu_visitantes()
      while choice5!=0:
        vi=Visitantes()
        if choice5==1:
          vi.allVisitantes()
          choice5 = menu_visitantes()
        elif choice5==2:
          vi.selectCPF()
          choice5 = menu_visitantes()
        elif choice5==3:
          vi.dataCreate()
          choice5 = menu_visitantes()
        elif choice5==4:
          vi.dataUpdate()
          choice5 = menu_visitantes()
        elif choice5==5:
          vi.delete()
          choice5 = menu_visitantes()
          continue
        elif choice5==0 or choice5==6:
          break
        else:
          print("Opção inválida.")
        choice5= menu_visitantes()
    
    #Posse veículos
    elif choice==6:
      choice6=menu_posseVeiculos()
      while choice6!=0:
        if choice6==1:
          p.all()
          choice6=menu_posseVeiculos()
        elif choice6==2:
          p.dataCreate()
          choice6=menu_posseVeiculos()
        elif choice6==3:
          p.delete()
          choice6=menu_posseVeiculos()
        elif choice6==0 or choice6==4:
          break
        else:
          print("Opção inválida.")
        choice6=menu_posseVeiculos()
          
    #Movimentações
    elif choice==7:
      choice7=menu_movimentacao()
      while choice7 != 0:
        if choice7 ==1:
          mov.all()
        elif choice7 == 2:
          mov.selectMovAbertas() 
        elif choice7 == 3:
          mov.dataCreate()
        elif choice7 == 4:
          mov.update()
        elif choice7 == 5:
          break
        choice7=menu_movimentacao()
    else:

      print("Opção inválida.")
    choice = menu_admin()

    

"""
O menu_principal agora se chama menu_admin
login de admin
Login: admin 
Senha: admin
Obs: a senha não é exibida enquanto digita, mas tá salvando, só apertar enter
login de porteiro
login: port
Senha: 1234
"""

nivel = u.loginInput()
if nivel == "1":
  opcoes_admin()
else:
  opcoes_porteiro()
