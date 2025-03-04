# Exercícios

import math
# Inteiros (int)
# 1.Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# 2.Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# 3.Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# 4.Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
'''
print('Exercicio 4) ')
try:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite o segundo número: '))
    divisao = n1/n2
    print(divisao)
except ZeroDivisionError: 
    print('integer division or modulo by zero')
except KeyboardInterrupt:
    print('Sem número inserido')
except ValueError:
    print('Você inseriu uma string.')
'''

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# 6. Números de Ponto Flutuante (float)
# 7. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 8. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 9. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 10. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 11. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
'''print('Exercicio 11)')
raio_circulo = float(input('Digite o raio: '))
area_circulo =math.pi * raio_circulo ** 2
print(f'{area_circulo:.2f}')
'''
# Strings (str)
# 12. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 13. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 14. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 15. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
'''
print('Exercicio 15)')
data_usuario = input('Insira uma data no formato dd/mm/aaa: ')
dia, mes, ano = data_usuario.split('/')
print('Dia', dia)
print('Mês', mes)
print('Ano', ano)
'''

# 16. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# Booleanos (bool)
# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.