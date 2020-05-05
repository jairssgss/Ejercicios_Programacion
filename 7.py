word = str(input("Palabra a guardar: "))
file_name = str(input("Nombre del archivo .txt: "))

texto = open(f'{file_name}.txt','w')
texto.write(word)