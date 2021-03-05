# if <condição>:
#       bloco verdadeiro

# Exemplo1
'''
a = 3
if a > 2:
    print(f"{a} é maior que 2")

# Short Hand
if a > 2: print(f"{a} é maior que 2")

# if<condição>:
#    verdadeiro
#  else:
#    false    

b = 3
if b % 2 == 0:
    print(f"{b} é par")
else:
    print(f"{b} é ímpar")

# Short hand
print(f"{b} é par") if b % 2 == 0 else print(f"{b} é ímpar")

# aninhadas
num = -1

if (num > 0):
    print(f"{num} é Positivo")
elif (num < 0):
    print(f"{num} é Negativo")
else:
    print(f"{num} é igual a 0")

# escreva uma função que receba três argumentos
1 - num1
2 - num
3 - Operação (mul, div, sub, adi)
4 - o resultado da operação

 Restam 1 minuto
'''
# entrada de dados
n1 = int(input("primeiro valor"))
n2 = int(input("segundo valor"))
op = input("terceiro valor")

# Definição da função
def resultado(n1,n2, op):
    #a = n1
    #b = n2
    if op == "soma":
        return n1 + n2
    elif op == "sub":
        return n1 - n2
    elif op == "mul":
        return n1 * n2
    elif op == "div":
        return n1 / n2
    else:
        return "por favor insira uma operação válida"
    

x = resultado(n1,n2,op)
print(x)
