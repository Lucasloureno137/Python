listaNomes = []

for i in range(2):
    nomes = str(input("Insira seu nome: "))
    listaNomes.append(nomes)

if 'nicolas' in listaNomes:
    print("Hmmmm, nicolas é nome de viadinho")
else:
    print(listaNomes)