nome1 = str(input('Olá, insira o primeiro nome: '))
nome2 = str(input('Olá, insira o segundo nome: '))
valorPessoa1 = []
valorPessoa2 = []


for custoPessoa1 in range(5):
    valorInseridoP1 = int(input('Olá {}, insira o valor da compra: '.format(nome1)))
    valorPessoa1.append(valorInseridoP1)

for custoPessoa2 in range(5):
    valorInseridoP2 = int(input('Olá {}, insira o valor da compra: '.format(nome2)))
    valorPessoa2.append(valorInseridoP2)

if valorPessoa1 > valorPessoa2:
    print('Olá {}, você gastou um total de R${} e gastou que mais que {}, que gastou {}'.format(nome1, sum(valorPessoa1), nome2, sum(valorPessoa2)))
elif valorPessoa2 > valorPessoa1:
    print('Olá {}, você gastou um total de R${} e gastou que mais que {}, que gastou {}'.format(nome2, sum(valorPessoa2), nome1, sum(valorPessoa1)))
else:
    print('{} e {} gastaram o mesmo total de {}'.format(nome1, nome2, valorPessoa1))   

    


    