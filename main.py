resultado = ""
while resultado == "":
    print("Ingresa un numero superior a 0 para hacer la descomposición")
    numero = int(input())
    if numero == 0:
       print("Es un 0")
    elif numero < 0:
        print("Es un número negativo")
    elif numero == 2:
        resultado = "Los números primos son: " + str(2)
    else:
        resultado = "Los números primos son: "
        acum = numero
        i = 2
        while acum>=2:
            result = acum % i
            if result == 0:
                acum = acum / i
                resultado = resultado + str(i) + "*"
                i = 2
            else:
                i = i + 1
print(resultado)