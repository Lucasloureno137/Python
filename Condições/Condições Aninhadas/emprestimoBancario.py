valorCasa = float(input('Insira o valor da casa: '))
salario = float(input('Insira o valor do salário: '))
anos = int(input('Em quantos anos será feito pagamento? '))
valorParcela = valorCasa/(anos*12)

print('30 por cento do salario corresponde a: {}'.format(salario*0.30))
print('O valor de cada parcela ficará em {:.2f}'.format(valorParcela))
if valorParcela > salario*0.30:
    print('Empréstimo negado')
else:
    print('Empréstimo aceito')
