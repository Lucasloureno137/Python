lista = [] #Cria uma lista vazia, onde posteriormente serão armazenados os valores inseridos pelo usuário

#Pede ao usuário que insira três vezes um nome
for i in range(3):
    ListaUser = str(input("Insira um nome: "))
    lista.append(ListaUser) #Atualiza a lista vazia com os valores inseridos pelo usuário

lista.pop(0)#Remove o primeiro valor da lista(0)
print(lista)

