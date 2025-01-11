salario = float(input('Insira o salário atual do funcionáio'))
porcReajuste = int(input('Insira a porcentagem adicional do salário: '))
reajusteOpc = porcReajuste/100
novoSalario = salario+reajusteOpc*salario

print('O salário de {} aumentou para {} com o reajuste'.format(salario,novoSalario))