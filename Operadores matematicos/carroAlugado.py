diasAlugados = int(input('O carro foi alugado por quantos dias? '))
kmPercorridos = int(input('Quantos kms o carro percorreu? '))
valorDiasAlugados = diasAlugados * 20
valorKmPercorridos = kmPercorridos * 0.15
valorTotal = valorDiasAlugados+valorKmPercorridos

print("O valor do aluguel ficou em R${}".format(valorTotal))