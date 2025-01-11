soma = 0

for i in range(1, 500+1):
    if i%2 != 0 and i%3 == 0:
        soma += i
print(soma)
        