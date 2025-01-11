import math

# Usamos math.radians(angulo) para converter o valor de graus para radianos.

angulo = float(input('Insira o ângulo a ser calculado: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O ângulo de {} graus tem o SENO de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(angulo,seno,cos,tan))