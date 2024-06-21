num = input("Ingrese un número de tres cifras: ")
if len(num) != 3:
    print("El número ingresado no tiene tres cifras.")
else:
    print(f"El segundo dígito del número ingresado es {num[1]}.")