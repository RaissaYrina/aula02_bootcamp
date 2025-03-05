# Exercícios

import math
# Inteiros (int)
# 1.Escreva um programa que soma dois números inteiros inseridos pelo usuário.
''''
print('Exercicio 1) ')
n1 = int(input("Insira o primeiro número: "))
n2 = int(input('Insira o segundo número: '))
soma = n1 + n2
print(f'A soma dos números {n1} e {n2} é {soma}')
'''
# 2.Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
'''
print('Exercicio 2) ')
CONSTANTE = 5
n1 = int(input("Insira um número: "))
resto = n1% CONSTANTE
print(f'O resto da divisão por {CONSTANTE} é {resto}')
'''
# 3.Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
'''
print('Exercicio 3) ')
n1 = int(input("Insira o primeiro número: "))
n2 = int(input('Insira o segundo número: '))
mult = n1 * n2
print(f'A multiplicação dos números {n1} e {n2} é {mult}')
'''
# 4.Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
'''
print('Exercicio 4) ')
try:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite o segundo número: '))
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
'''
print('Exercicio 5) ')
n1 = int(input("Insira o primeiro número: "))
num_quadrado = n1 ** 2
print(f'O quadrado do número {n1} é {num_quadrado}')
'''

#Números de Ponto Flutuante (float)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
'''
print('Exercicio 6)')
n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
soma = n1 + n2
print(f'A soma dos números {n1} e {n2} é {soma}')
'''
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
'''
print('Exercicio 7)')
n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
media = (n1 + n2) / 2
print(f'A média é {media}')
'''
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
'''
print('Exercicio 8)')
base = float(input('Insira um número para base da potência:  '))
expoente = float(input('Insira um número para o expoente da potência: '))
potencia = base ** expoente
print(f'O Resultado da potência é {potencia}')
'''
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
'''
print('Exercicio 9)')
celsius = float(input('Insira o valor da temperatura em graus celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'{celsius}°C equivale a {fahrenheit}°F')
'''
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
'''
print('Exercicio 10)')
raio_circulo = float(input('Digite o raio: '))
area_circulo =math.pi * raio_circulo ** 2
print(f'{area_circulo:.2f}')
'''

# Strings (str)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
'''
print('Exercicio 11)')
texto = input('Insira um texto: ')
maiscula = texto.upper()
print(maiscula)
'''
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
'''
print('Exercicio 12)')
texto = input('Insira um texto: ')
minuscula = texto.lower()
print(minuscula)
'''
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
'''
print('Exercicio 13)')
texto = input('Insira um texto: ')
frase_sem_espaco = texto.strip()
print(frase_sem_espaco)
'''
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
'''
print('Exercicio 14)')
data_usuario = input('Insira uma data no formato dd/mm/aaa: ')
dia, mes, ano = data_usuario.split('/')
print('Dia', dia)
print('Mês', mes)
print('Ano', ano)
'''
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
'''
print('Exercicio 15)')
parte1 = input('Digite um texto: ')
parte2 = input('Digite outro texto: ')
concatenacao = parte1 + " " + parte2 
print(concatenacao)
'''
# Booleanos (bool)
# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
'''
print('Exercicio 16)')
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)
'''
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
'''
print('Exercicio 17)')
valor1 = True
valor2 = False
resultado_and = valor1 or valor2
print("Resultado do AND lógico:", resultado_and)
'''
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
'''
print('Exercicio 18)')
valor = input("Digite um valor booleano (True ou False): ")
valor_booleano = valor.strip().lower() == "true"
valor_invertido = not valor_booleano
print(f"O valor invertido é: {valor_invertido}")
'''
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
'''
print('Exercicio 19)')
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
check_numero = n1 == n2
print(f"Resultado da igualdade: {check_numero}")
'''
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print('Exercicio 20)')
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
check_numero = n1 != n2
print(f"Resultado da igualdade: {check_numero}")


#Aqui estão cinco exercícios que envolvem TypeError, verificação de tipo (type check), 
# o uso de try-except para tratamento de exceções e a utilização da estrutura condicional if. 
# Esses exercícios aumentam progressivamente em dificuldade e abordam situações práticas 
# onde você pode aplicar esses conceitos.

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) 
# do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para 
# classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da 
# lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, 
# imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, 
# imprima a lista de inteiros.