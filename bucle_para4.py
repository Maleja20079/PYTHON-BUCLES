valor_x = int(input("Ingrese el valor maximo para x: "))

while valor_x < 0:
    valor_x = int(input("No puede ser negativo. Intente de nuevo: "))

for x in range(0, valor_x + 1, 2):
    func = x ** 3 + x ** 2 - 5
    print("Para x =", x, "f(x)=", func)