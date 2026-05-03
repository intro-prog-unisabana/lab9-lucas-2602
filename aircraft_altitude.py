from aircraft import Aircraft
modelo = input("Enter aircraft model: ")
maquina = Aircraft(modelo)
while True:
    comando = input("Enter command (A for ascent, D for descent, X to exit): ")
    if comando.upper() == "X":
        break
    parts = comando.split()
    altitud = parts[0]
    unidades = int(parts[1])

    if altitud.upper() == "A":
        maquina.climb(unidades)

    elif altitud.upper() == "D":
        maquina.descend(unidades)

print(f"Final altitude: {maquina.altitude} feet")
