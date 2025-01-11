num = int(input('Insira um número inteiro qualquer: '))
cont1 = 0
cont2 = 0
for i in range(1,num+1):
    if i > 0 and i % 2 == 0:
       cont1 += 1
    else:
       cont2 += 1
    

print('O total de números pares na sequência é {}'.format(cont1))
print('O total de números ímpares na sequência é {}'.format(cont2))



    
    
   