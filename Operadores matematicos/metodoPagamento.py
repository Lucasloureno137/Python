valorProduto = float(input('Insira o valor do produto: '))
FormaPagamento = int(input('Qual a forma de pagamento desejada? (1-Pix a vista ou dinheiro 15%, 2-A vista cartão de crédito 10%, 3- parcelado em duas vezes, 4- parcelado em 3 ou mais vezes juros de 10%)'))
pix = (valorProduto*0.15) - valorProduto
credito = (valorProduto*0.10) - valorProduto
parcela3x = (valorProduto*0.10) + valorProduto
valorParcela = parcela3x/3


if FormaPagamento == 1 :
    print(pix)
elif FormaPagamento == 2 :
    print(credito)
elif FormaPagamento == 3 :
    print(valorProduto)
elif FormaPagamento == 4 :
    print('O valor total é de {} e o de cada parcela é {:.2f}' .format(parcela3x,valorParcela))
