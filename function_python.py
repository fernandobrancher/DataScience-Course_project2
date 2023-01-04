def cadastro_produto(database, id_produto, nome, dados, quantidade, descricao):
  dict_cadastro = {
    'ID': id_produto,
    'Nome': nome,
    'Especificações': dados,
    'Quantidade': quantidade,
    'Descrição': descricao,
  }
  database.append(dict_cadastro)
  print("\nCadastrado com sucesso\n")
  return database

def id_livre(id_produto, database):
  for dicionario in database:
    if int(dicionario['ID']) == int(id_produto):
      print("Esse ID já existe")
      return False
  return True

def id_valido(id_produto, database):

  for dicionario in database:
    if int(dicionario['ID']) == int(id_produto):
      return True
  print("ID não encontrado")
  return False

def consultar_produto(id_produto,database):
  for dicionario in database:
    if int(dicionario['ID']) == int(id_produto):
      print(f'ID: {dicionario["ID"]}')
      print(f'Nome: {dicionario["Nome"]}')
      dados = dicionario["Especificações"]
      txt = dados.split(":")
      txt.pop(-1)
      if len(txt) > 0:
        for dados in txt:
          dado = dados.split(",")
          print(f'{dado[0]}: {dado[1]}')
      print(f'Quantidade: {dicionario["Quantidade"]}')
      if len(dicionario["Descrição"].strip(" ")) != 0:
        print(f'Descrição: {dicionario["Descrição"]}')

def listar_produtos(database):
  if database != []:
    for dicionario in database:
      print(f'ID: {dicionario["ID"]} | Nome: {dicionario["Nome"]}.')
    print('\n')
  else:
    print("Lista Vazia")


def remove_cadastro(id_produto, database):
  for dicionario in database:
    if int(dicionario['ID']) == int(id_produto):
      database.remove(dicionario)
  print(f'Produto de ID: {id_produto} removido com sucesso. \n')
  return database

