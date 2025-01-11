salarioMinimo = 1293.20
valorSalario = float(input('Insira o valor do seu salário'))
numeroSalariosMinimo = valorSalario/salarioMinimo

print('Você recebe R${} e isso corresponde a {:.2f} salários minimos'.format(valorSalario,numeroSalariosMinimo))