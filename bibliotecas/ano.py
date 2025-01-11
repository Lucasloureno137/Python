from datetime import datetime

# Solicita o ano de nascimento
ano_nascimento = int(input('Insira o ano em que você nasceu: '))
mes_nascimento = int(input('Insira o mês em que você nasceu (1-12): '))
dia_nascimento = int(input('Insira o dia em que você nasceu (1-30): '))

# Data atual
data_atual = datetime.now()

# Data de nascimento
data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)

# Diferença entre a data atual e a data de nascimento em dias
diferenca_dias = (data_atual - data_nascimento).days

# Calcula os anos, meses e dias vividos
anos_vividos = diferenca_dias // 365
dias_restantes = diferenca_dias % 365
meses_vividos = dias_restantes // 30
dias_vividos = dias_restantes % 30

# Imprime o resultado
print(f'Você viveu {anos_vividos} anos, {meses_vividos} meses e {dias_vividos} dias.')


