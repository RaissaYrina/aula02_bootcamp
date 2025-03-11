#Desafio - Refatorar o projeto da aula anterior evitando Bugs!
#Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas
#  para um número de ponto flutuante e prevenção de valores negativos para salário e bônus, 
# você pode modificar o código diretamente. 
# Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que 
# os valores sejam positivos.

BONUS_CONT = 1000

#1. Solicite o nome do usuario
try:
    nome = input("Digite o seu nome: ")

    if len(nome) == 0:
        raise ValueError('O nome não pode estar vazio')
    elif nome.isdigit():
        raise ValueError('O nome não deve ser um digitos')
    else:
        print(f'Nome válido: {nome}')
except ValueError as e:
    print(e)
    
#2. Digite o seu salario
try:
    salario = float(input("Digite o seu salário: "))
    if salario < 0:
        print('Por favor, digite um valor positivo para o salario')
except ValueError:
    print('Entrada inválida')
    
#3. Digite o valor do bonus recebido 
try: 
    bonus = float(input("Digite o valor do seu bônus: "))
    if bonus < 0: 
        print('Por favor, digite um valor positivo para o bonus recebido: ')
except ValueError:
    print('Entrada inválida para bônus recebido')


#4. Calcule o valor do bonus final 
valor_bonus = BONUS_CONT + salario * bonus 

#6. mensagem personalizada
print(f' Olá! {nome} muito bom te ter por aqui! \n você possui o bonus de R${valor_bonus}')
