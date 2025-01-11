frase = str(input('Insira uma frase')).lower() #recebe a frase e converte pra minusculo pra evitar erros
contador = {} # armazena a contagem das letras em um dicionario


for char in frase: #analisa a frase, letra a letra
    if char in frase: #confere se a letra aparece na frase
        if char in contador: #se a letra já estiver no contador, se adiciona 1 ao seu valor, se não, apenas se inicia como 1
            contador[char] += 1
        else:
            contador[char] = 1
        
        
            
for letras, quantidade in contador.items():
    if letras == ' ':
        print(f"A frase possui {quantidade} espaços.")
    else:
        print(f"A letra '{letras}' aparece {quantidade} vezes.")
        
# A ultima linha define as letras como chaves, e a quantidade como os valores dessas chavesmorom

