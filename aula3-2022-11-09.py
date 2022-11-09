print("Início da aula 3 (09/11/2023)")

contador = 1

while(contador <= 10):
  print(contador)
  contador = contador+1 #contador += 1

#Laço for (pytho for = for each)

fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

#Lista
frutas = ["morango", "laranja", "pêra"]
print(frutas)

#Quero exibir apenas a terceira fruta (pêra)
print(frutas[2])

#Exibir quantas frutas tem na minha lista?
print(len(frutas)) #legth = tamanho

#Quero incluir uma fruta nova
frutas.append("manga") #"pop" para remover fruta

print(len(frutas)) #legth = tamanho
print(frutas)
print(frutas[0]) 
print(frutas[1]) 
print(frutas[2]) 
print(frutas[3]) 
#print(frutas[4]) 

print("Exemplos das frutas com while...")
frutas.append("uva")

i=0 #(i de index)
while(i-4):  
  print(frutas[i])
  i = i + 1
