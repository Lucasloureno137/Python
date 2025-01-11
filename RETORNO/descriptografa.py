text_criptografado = str(input('Insira o texto criptografado'))  # Texto já criptografado
shift = 3  # Mesmo valor usado para criptografar
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text_original = ''  # Variável para armazenar o texto descriptografado

for char in text_criptografado:  # Itera sobre cada caractere do texto criptografado
    if char == ' ':  # Verifica se o caractere é um espaço
        text_original += char  # Adiciona o espaço diretamente ao texto descriptografado
    else:
        index = alphabet.find(char)  # Encontra o índice da letra criptografada no alfabeto
        new_index = index - shift  # Subtrai o deslocamento (shift) para retornar à posição original
        new_index %= len(alphabet)  # Garante a rotação no alfabeto (caso o índice fique negativo)
        text_original += alphabet[new_index]  # Adiciona a letra descriptografada ao texto final

print('Texto descriptografado: {}'.format(text_original))  # Exibe o resultado final