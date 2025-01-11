import random

listaMoeda = ['cara','coroa']
escolhaUsuario = str(input('cara ou coroa?'))
escolhaPC = random.choice(listaMoeda)

print('O resultado foi {} e você escolheu {}' .format(escolhaPC,escolhaUsuario))