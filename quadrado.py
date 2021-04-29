n = int(input(": "))
quadrado = []
for e in range(1, n+1):
    m = input("linha %i: "%e).split()
    aux = []
    for k in m:
        aux.append(int(k))
    quadrado.append(aux)

#Acha linha errada
soma = sum(quadrado[0])
diferente1 = 0
linha_errada = 0

for linha in range(len(quadrado)):
    s = sum(quadrado[linha])
    if s != soma and diferente1 == 0:
        diferente1 = s
        linha_errada = linha
    elif s != soma and diferente1 != 0:
        soma = s
        diferente1 = sum(quadrado[0])
        linha_errada = 0

#Acha coluna errada
soma_coluna = 0
diferente2 = 0
coluna_errada = 0
for i in range(len(quadrado)):
    soma_coluna+= quadrado[linha_errada][i]

    for coluna in quadrado:
        if coluna != quadrado[linha_errada]:
            soma_coluna+= coluna[i]
    if soma_coluna != soma:
        diferente2 = soma_coluna
        coluna_errada = i
        break
    soma_coluna = 0

errado = quadrado[linha_errada][coluna_errada]
if soma_coluna > soma:
    verifica = soma_coluna - soma
    correto = errado - verifica
else:
    verifica = soma - soma_coluna
    correto = verifica + errado

print(correto, errado)