#Criação de funções

preco = 1999.90

#Calcular 5% de imposto, guardar na variável imposto e exibir na tela

imposto = preco * 0.05
print(preco)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcula_imposto() que calcular imposto de 5% e retorna a quem pediu...
#Isso é a declaração da função (Como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso... aqui é o imposto a calcular... e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

#Explicação de variável local x global
print(preco) #???
preco_produto = 100
print(preco_produto) #???

#Agora calcular imposto a alíquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515,5]
#Se eu quiser calcular o impostos destes quatro valores... e exibir na tela assim: "O imposto de... é ..." (1o. preco, 20. imposto)
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")