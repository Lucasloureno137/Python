text = str(input('Insira o texto que deseja criptografar: '))
shift = 3 #Representa o número de posições que cada letra será deslocada no alfabeto. 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text_criptografado = ''

for char in text.lower(): # transforma o conteúdo da variável em letras minúsculas
    if char == ' ':
        text_criptografado += char 
    else: 
        index = alphabet.find(char) # Printa os caracteres da varíavel separadamente
        new_index = (index + shift) % 26 # Soma o valor do deslocamento (shift) ao índice atual (index) da letra, calculando a nova posição no alfabeto após o deslocamento, O % 26 é o que mantém o índice dentro dos limites do alfabeto e permite que o deslocamento funcione corretamente.
        text_criptografado += alphabet[new_index] # Usa o novo índice (new_index) para encontrar o caractere correspondente na string alphabet
        print('char:', char, 'text criptografado:', text_criptografado) # Exibe o caractere original (char) e o caractere resultante (new_char) após o deslocamento
