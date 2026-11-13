votos_android = 0
votos_ios = 0
invalidos = 0

while True:
    codigo = int(input("Ingrese su código de estudiante (0 para terminar): "))

    if codigo != 0:
        opcion1 = int(input("Elija la plataforma: 1 = Android, 2 = iOS: "))

        if opcion1 == 1:
            votos_android = votos_android + 1
        elif opcion1 == 2:
            votos_ios = votos_ios + 1
        else:
            print("Plataforma no disponible. Su voto no será tenido en cuenta.")
            invalidos = invalidos + 1

    if codigo == 0:
        break

print("----- RESULTADOS -----")
print("Votos Android:", votos_android)
print("Votos iOS:", votos_ios)
print("Votos no válidos:", invalidos)

if votos_android > votos_ios:
    print("La plataforma elegida es Android.")
elif votos_ios > votos_android:
    print("La plataforma elegida es iOS.")
else:
    print("Hay empate. Se debe usar otro mecanismo de elección.")