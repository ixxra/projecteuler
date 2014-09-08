l = range(400, 450)

numeros_separados = []


for v in l:
    digitos = []
    y = v
    for k in range(4, -1, -1):
        digitos.append(y/10**k)
        y = y % 10**k
    numeros_separados.append(digitos)
