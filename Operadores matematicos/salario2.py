valorSalario = float(input('Insira o valor do salário atual: '))
porcAumento = int(input('Insira a porcentagem de aumento'))
PorcSalarioAumento = porcAumento/100
novoSalario = valorSalario+PorcSalarioAumento * valorSalario

print('O valor do novo salário é de {}' .format(novoSalario))