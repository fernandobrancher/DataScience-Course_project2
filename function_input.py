def receber_id():
  while (True):
    id_produto = input('Digite o ID do produto: ')
    try:
      id_produto = int(id_produto)
    except ValueError:
      print("Erro: ID inválido. O ID precisa ser um número inteiro.")
    else:
      return id_produto

def receber_nome():
  while(True):
    nome = input('Digite o nome do produto: ')
    if len(nome.strip(" ")) == 0:
      print("O campo nome está vazio\n")
    else:
      return nome

def receber_especificacoes():
  dados = ""
  inserir_dados = input('Você deseja inserir dados do produto? \nDigite S para inserir ou N para pular essa etapa: ').upper()
  while True:

    if inserir_dados == 'S':
      tipo = input('Digite o tipo da informação (ex.: marca, cor...): ')
      valor = input(f'Digite o valor do(a) {tipo}:')
      if len(tipo.strip(" ")) == 0 or len(valor.strip(" ")) == 0:
        print("Um ou mais campos está Vazio")
      else:
        dados = dados + tipo + "," + valor + ':'
      inserir_dados = input('Você deseja inserir dados do produto ? \nDigite S para inserir ou N para sair essa etapa: ').upper()
    elif inserir_dados == 'N':
      break
    else:
      inserir_dados = input("Opção inválida!\nDigite S para inserir ou N para sair essa etapa: ").upper()
  return dados

def receber_qtde():
    try:
      qtde = float(input('Digite a quantidade do produto em estoque:'))
      return qtde
    except ValueError:
      print('Valor Inválido. A quantidade precisa ser um valor numérico.')
      return receber_qtde()    

def receber_descricao():
  inserir_descricao = input('Você deseja inserir uma descrição para o produto? \nDigite S para inserir ou N para pular essa etapa: ').upper()
  while not (inserir_descricao== 'S' or inserir_descricao == 'N'):
    
    inserir_descricao = input("Opção inválida!\nDigite S para inserir ou N para sair essa etapa: ").upper()

  if inserir_descricao == "S":
    texto = input('Insira a descrição para o produto: ')
    if len(texto.strip(" ")) == 0:
      print("Produto sem Descrição")
      texto = ""
  elif inserir_descricao == "N":
    texto = ""
  return texto
