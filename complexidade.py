# -*- coding: UTF-8 -*-
codigo = input("").split()
codigo_final = []
loops = []
custo = 0
somaloop = 0
soma = 0

for i in codigo:
    if i.isalpha():
        codigo_final.append(i)
    elif i.isnumeric():
        codigo_final.append(int(i))

for i in range(len(codigo_final)):
    if codigo_final[i] == "LOOP":
        loops.append(codigo_final[i])
        loops.append(codigo_final[i+1])
    elif codigo_final[i] == "OP":
        if len(loops) == 0:
            custo+= codigo_final[i+1]
        elif len(loops) == 2:
            somaloop = codigo_final[i+1]
            somaloop*= loops[-1]
            custo+= somaloop
        else:
            somaloop = codigo_final[i+1]
            somaloop*= loops[-1]
            soma+= somaloop
    elif codigo_final[i] == "FIMLOOP":
        if len(loops) == 2:
            soma = soma*loops[-1]
            custo+= soma
            loops.pop(-1)
            loops.pop(-1)
            soma = 0
        else:
            loops.pop(-1)
            loops.pop(-1)

print(custo)