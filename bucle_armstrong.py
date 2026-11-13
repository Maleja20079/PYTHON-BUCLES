num = int(input("Ingrese un número entero positivo: "))

while num <= 0:
    num = int(input("Debe ser positivo. Intente de nuevo: "))

copia1 = num
cantidad = 0
while copia1 > 0:
    cantidad = cantidad + 1
    copia1 = copia1 // 10

copia1 = num
suma = 0
while copia1 > 0:
    digito = copia1 % 10
    suma = suma + digito ** cantidad
    copia1 = copia1 // 10

if suma == num:
    print(num, "Sí es un número de Armstrong")
else:
    print(num, "NO es un número de Armstrong")