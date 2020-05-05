hora = 300
jornada = 8 * hora
dias = int(input("\nIngresa los dias laborados: "))
total_ganado = dias * jornada
if dias > 0:
    print(f"\nGanaste en total ${total_ganado} pesos por tus {dias} días laborados.\n")
else:
    print("\nNo ha generado ingresos $$$.\n")