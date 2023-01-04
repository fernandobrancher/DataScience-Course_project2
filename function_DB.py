import csv

def ler_DB():
  try:
    with open('arquivo.csv','r') as arquivo:
      leitor = csv.DictReader(arquivo, delimiter = ';', lineterminator='\n')
      tabela = []
      for linha in leitor:
        tabela.append(linha)
    return tabela
  except FileNotFoundError:
    print("É necessario abrir uma arquivo")
    with open('arquivo.csv', 'w', newline='\n') as arquivo:
      arquivo.write("ID;Nome;Especificações;Quantidade;Descrição")
    lista = []
    return lista

def update_DB(database):
  try:
    campos = list(database[0].keys())
    with open('arquivo.csv', 'w', newline='\n') as arquivo:
      escritor = csv.DictWriter(arquivo, delimiter = ';',fieldnames = campos)
      escritor.writeheader()
      for linha in database:
        escritor.writerow(linha)
    return
  except IndexError:
    with open('arquivo.csv', 'w', newline='\n') as arquivo:
      arquivo.write("ID;Nome;Especificações;Quantidade;Descrição")
    return
    

