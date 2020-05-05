orden = []
for x in range(1,11):
    numero = int(input(f"Ingresa el número {x}:  "))
    orden.append(numero)
orden.sort(reverse=True)
print(orden)