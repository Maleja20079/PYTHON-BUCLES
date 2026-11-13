cant_term = int(input("Ingrese la cantidad de terminos a generar: "))

term = 1

for cont_num in range(1, cant_term):
    print(term)
    term = term + 2

print(term)