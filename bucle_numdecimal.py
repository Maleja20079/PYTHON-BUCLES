num = int(input("INGRESE UN NÚMERO ENTERO: "))

if num > 0:
    copia_numero = num
    contador_cifra = 0
    suma_cifra = 0

    while copia_numero > 0:
        cifra = copia_numero % 10
        copia_numero = copia_numero // 10
        suma_cifra = suma_cifra + cifra
        contador_cifra = contador_cifra + 1

    print("La cantidad de cifras de", num, "son", contador_cifra)
    print("La sumatoria es:", suma_cifra)

else:
    print("No es un número positivo")