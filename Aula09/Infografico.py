contador = 0
for numero in range (100):
    if (numero % 2) == 0:
        contador += 1
    print(contador)

acumulador = 0
for numero in range (100):
    if (numero % 2) == 0:
        acumulador += numero
print(acumulador)