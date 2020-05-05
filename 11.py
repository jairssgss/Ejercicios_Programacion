decimales = []
enteros={1:'uno',2:'dos',3:'tres',4:'cuatro',5:'cinco',6:'seis',7:'siete',8:
'ocho',9:'nueve',10:'diez'}

flotante = float(input("Ingresa un flotante: "))
decimales.append(flotante)
rango = flotante

while rango>1 and rango<10:
    rango = float(input("Ingresa un flotante: "))
    decimales.append(rango)
    if len(decimales) == 5:
        break
   
decimales.sort()

if len(decimales)<5:
    print("Fuera de rango.")

if decimales[0]<1:
    decimales.pop(0)
elif decimales[-1]>10:
    decimales.pop(-1)
else:
    pass

print("Número mayor introducido: ",enteros[int(decimales[-1])])


        
