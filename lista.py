import math
####criando um dicionario de produtos###
_listaDeProdutos = [{"item": "Escova de dentes","quantidade": 3, "precoUnitario": 40.60},{"item": "Shampoo","quantidade": 1, "precoUnitario": 35.50},
  {"item": "Sabonete","quantidade": 3, "precoUnitario": 10.97},
  {"item": "Aspirina","quantidade": 3, "precoUnitario": 13.99}]
####criando uma lista de emails###
_listaEmails=['ncatundafr@gmail.com','asdf@gmail.com','qwertyuiop@yahoo.com']
####calculando o item pela chave do produto###
def calculaPrecoProduto(item):
  return item["quantidade"]*item["precoUnitario"]

def listaPrecoTotalporEmail(listaDeProdutos,listaEmails):
  #### chamando a função calculaPrecoProduto para executar o mesmo em listadeProdutos###
  listaPrecoProdutos = list(map(calculaPrecoProduto,listaDeProdutos)) 
  ##### somando a quantidade do preco pela soma de itens da lista ###
  precoTotal = math.fsum(listaPrecoProdutos)
  ####transformando o valor em decimal e dividindo o preco pelo tamanho de uma lista de emails####
  precoPorEmail = "{:.2f}".format(precoTotal/len(listaEmails))
  ###retorna outra função que chama email e o preço total por email na listaPrecoTotalporEmail##
  return list(map(lambda email: {"email": email ,"preco": precoPorEmail}, listaEmails))
 ##printando os valor da função e chamando o dicionario e a lista####
print(listaPrecoTotalporEmail(_listaDeProdutos,_listaEmails))



