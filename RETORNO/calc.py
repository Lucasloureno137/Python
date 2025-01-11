listaValores = [] #Lista vazia

for i in range(5):
    valores = int(input("Insira um valor "))
    listaValores.append(valores)

somaListaValores = sum(listaValores) #Função SUM consegue somar todos os valores dentro de uma lista
print(somaListaValores)