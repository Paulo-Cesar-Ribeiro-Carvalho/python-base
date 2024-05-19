#!/usr/bin/env python3
"""Calculadora prefix.

funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefix.py sum 5 2
7

$ prefix.py mul 10 5
50

$ prefix.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"

#Pra receber os argumentos que o usário passar é preciso importar o sys.
#Pra pegar os argumentos cria uma variável arguments...

import sys
arguments = sys.argv[1:]

#if not arguments (se eu não tiver argumento nenhum qual a operação...)
#No elif (se o tamanho dos argumentos for diferente de 3 esta invalido)
if not arguments:
    operation = input("escolha uma operação e digite Enter: ")
    n1 = input("Digite o primeiro número: ") 
    n2 = input("Digite o segundo número: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments
# fazer uma tupla contendo os itens abaixo para validar
valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida!")
    print(valid_operations)
    sys.exit(1)

#validar os números
validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit(): #para permitir float usa o replace
        print(f"Número invalido {num}") #adicionar placeroder sempre com f na frente
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
        
n1, n2 = validated_nums #unpacking do validated_nums

#TODO: Usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado é: {result}")
