vocales = ['a','e','i','o','u','A','E','I','O','U',' ']

palabra = str(input("Ingresa una palabra: "))

for letra in palabra:
    for vocal in vocales:
        if letra == vocal:
            palabra = palabra.replace(letra,'')
#print(palabra)
print("No. de Consonantes: ",len(palabra))

