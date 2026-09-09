try:

    numero = int(input("Ingresa un numero entero:"))
    print(f"Ingresaste el numero:{numero}")

except ValueError:
    print ("Error: El dato ingresado es incorrecto. Debe ser un numero entero.")    