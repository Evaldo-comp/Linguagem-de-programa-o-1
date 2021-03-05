# While
# while<condicao>:
#    bloco
'''
x = 1
while x <= 3:
    print(x)
    x +=1

# break

alunos = ["Marcelo", "Bruna", "Jonas", "Edinara", "Vitória"]
cont = 0

while(cont <= (len(alunos))):
    if alunos[cont] == "Edinara":
        print(f"{alunos[cont]} Faltou")
        break
    print(f"{alunos[cont]} Presente")
    cont += 1
'''

# continue
 i = 0
 while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)