from function_DB import *
from function_input import *
from function_python import *

lista_DB = ler_DB()

while (True):
  menu = input(
    "\nBoas vindas ao nosso sistema - Escolha uma das opções para continuar:\n\n1 - Cadastrar produto\n2 - Consultar produto\n3 - Listar produtos cadastrados\n4 - Atualizar cadastro\n5 - Excluir cadastro\n6 - Sair\n\n"
  )
  if menu == '1':
    id_produto = receber_id()
    if id_livre(id_produto,lista_DB):
      nome = receber_nome()
      dados = receber_especificacoes()
      qtde = receber_qtde()
      texto = receber_descricao()
      lista_DB = cadastro_produto(lista_DB, id_produto, nome, dados, qtde, texto)
      update_DB(lista_DB)

  elif menu == '2':
    id_produto = receber_id()
    if id_valido(id_produto, lista_DB):
      consultar_produto(id_produto, lista_DB)

  elif menu == '3':
    listar_produtos(lista_DB)

  elif menu == '4':
    id_produto = receber_id()
    if id_valido(id_produto, lista_DB):
      lista_DB = remove_cadastro(id_produto, lista_DB)
      nome = receber_nome()
      dados = receber_especificacoes()
      qtde = receber_qtde()
      texto = receber_descricao()
      lista_DB = cadastro_produto(lista_DB, id_produto, nome, dados, qtde, texto)
      update_DB(lista_DB)

  elif menu == '5':
    id_produto = receber_id()
    if id_valido(id_produto, lista_DB):
      lista_DB = remove_cadastro(id_produto, lista_DB)
      update_DB(lista_DB)

  elif menu == '6':
    break
  else:
    print('Valor inválido')
