import statistics

lista = []

cantidad = int(input("¿Cuántos números ingresarás?\nRespuesta:      "))

for x in range(1,cantidad+1):
    num = int(input(f"Número {x}:     "))
    lista.append(num)

lista.sort()

print("Números ingresados: ",lista)
print("Media:   ", round(statistics.mean(lista),2))
print("Moda:    ",statistics.mode(lista))
print("Desviación estándar:    ",round(statistics.stdev(lista),2))