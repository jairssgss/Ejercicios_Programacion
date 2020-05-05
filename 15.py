def esPrimo(numero):
    if numero<2:
        return False

    for internos in range(2,numero):
        if numero%internos == 0:
            return False

    else:
        print(numero)


lista_primos = []

for i in range(1,11):
    nums = int(input(f"Número {i}:   "))
    lista_primos.append(nums)
lista_primos.sort()
print(lista_primos)

for x in lista_primos:
    esPrimo(x)