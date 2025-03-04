#Desafio - Refatorar o projeto da aula anterior evitando Bugs!
#Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas
#  para um número de ponto flutuante e prevenção de valores negativos para salário e bônus, 
# você pode modificar o código diretamente. 
# Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que 
# os valores sejam positivos.

BONUS_CONT = 1000

#1. Solicite o nome do usuario
nome = input("Digite o seu nome: ")
if nome.isdigit():
    print("Você digitou o seu nome errado")
    exit()

elif len(nome) == 0 or nome.isspace():
    print('Você não digitou nada')
    exit()
else:
    print(nome)

'''
#2. Digite o seu salario
salario = float(input("Digite o seu salário: "))

#3. Digite o valor do bonus recebido 
bonus = float(input("Digite o valor do seu bônus: "))

#4. Calcule o valor do bonus final 
valor_bonus = BONUS_CONT + salario * bonus 

#6. mensagem personalizada
print(f' Olá! {nome} muito bom te ter por aqui! \n você possui o bonus de {valor_bonus}')
'''