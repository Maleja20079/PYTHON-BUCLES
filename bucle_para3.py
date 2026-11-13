cant_num = int(input("Ingrese la cantidad de numeros: "))

while cant_num < 0:
    cant_num = int(input("No puede ser negativo. Intente de nuevo: "))

for num in range(1, cant_num + 1):
    print(num, " ", num * num, " ", num + num * num)