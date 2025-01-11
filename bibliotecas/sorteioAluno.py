import random

aluno1 = str(input('Insira o nome do aluno 1: '))
aluno2 = str(input('Insira o nome do aluno 2: '))
aluno3 = str(input('Insira o nome do aluno 3: '))
aluno4 = str(input('Insira o nome do aluno 4: '))

listaAlunos = [aluno1 , aluno2 , aluno3 , aluno4]

#Embaralha a lista 
random.shuffle(listaAlunos)

alunoEscolhido = random.choice(listaAlunos)
print(alunoEscolhido)
print(listaAlunos)

