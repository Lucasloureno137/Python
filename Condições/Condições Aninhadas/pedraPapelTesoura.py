import random

lista = ['pedra', 'papel', 'tesoura']
escolhaSorteada = random.choice(lista)
escolha = str(input('Insira sua jogada  (pedra,papel ou tesoura): '))

if escolha == 'papel' and escolhaSorteada == 'pedra':
    print('O computador escolheu {} e você escolheu {}, você ganhou!!'.format(escolhaSorteada,escolha))
elif escolha == 'papel' and escolhaSorteada == 'papel':
    print('O computador escolheu {} e você escolheu {}, empatou!!'.format(escolhaSorteada,escolha))
elif escolha == 'papel' and escolhaSorteada == 'tesoura':
    print('O computador escolheu {} e você escolheu {}, você perdeu!!'.format(escolhaSorteada,escolha))
elif escolha == 'pedra' and escolhaSorteada == 'tesoura':
    print('O computador escolheu {} e você escolheu {}, você ganhou!!'.format(escolhaSorteada,escolha))
elif escolha == 'pedra' and escolhaSorteada == 'pedra':
    print('O computador escolheu {} e você escolheu {}, você empatou!!'.format(escolhaSorteada,escolha))
elif escolha == 'pedra' and escolhaSorteada == 'tesoura':
    print('O computador escolheu {} e você escolheu {}, você perdeu!!'.format(escolhaSorteada,escolha))
elif escolha == 'tesoura' and escolhaSorteada == 'papel':
    print('O computador escolheu {} e você escolheu {}, você ganhou!!'.format(escolhaSorteada,escolha))
elif escolha == 'tesoura' and escolhaSorteada == 'tesoura':
    print('O computador escolheu {} e você escolheu {}, você empatou!!'.format(escolhaSorteada,escolha))
elif escolha == 'tesoura' and escolhaSorteada == 'pedra':
    print('O computador escolheu {} e você escolheu {}, você perdeu!!'.format(escolhaSorteada,escolha))



