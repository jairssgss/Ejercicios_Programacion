aux = -1
nombre = ['G','i','n','e']
while aux < 4:
    respuesta=str(input("¿Quién es la mamá de Gokú?\nRespuesta:   "))
    mama=respuesta.lower()
    if mama == 'gine':
        print("Respuesta correcta!")
        aux = 5
    else:
        aux+=1
        if aux == 4:
            print("Intentos agotados, respuesta: Gine.")
            break
        else:
            print("Pista: ",nombre[aux])
