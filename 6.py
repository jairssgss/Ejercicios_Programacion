#'w' modo write, escribir texto en el archivo.


#Pedimos la palabra.
p = str(input("Palabra a guardar: ")) 

#Asignamos el nombre del archivo y el modo en el que trabajaremos.
a = open('texto_en_py.txt','w')

#La palabra recibida se guarda en el archivo.
a.write(p)
