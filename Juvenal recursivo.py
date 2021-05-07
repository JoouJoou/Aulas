def Gn(n, g = 0):
    if n == 1:
        g = g+1
        return gk
    elif n%2 == 0:
        n = n/2
        g = g+1
        return Gn(n, g)
    elif n%2 != 0:
        n = (n*3)+1
        g = g+1
        return Gn(n, g)
a = Gn(9)
print(a)
"""testes = int(input(": "))
count = 1
while count != testes:"""