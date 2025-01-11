salarioAtual = float(input('Insira seu salário atual: '))

if salarioAtual > 1250.0:
    print(salarioAtual*0.10+salarioAtual)
elif salarioAtual <= 1250.0:
    print(salarioAtual*0.15+salarioAtual)