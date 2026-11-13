n = int(input("Ingrese un número entero: "))

if n < 0:
    print("Los números negativos no tienen factorial.")
else:
    factorial = 1
    contador = 1

    if n > 1:
        while True:
            factorial = factorial * contador
            contador = contador + 1
            if contador > n:
                break

    print(n, "! =", factorial)