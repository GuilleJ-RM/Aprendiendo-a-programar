sueldo_por_horas = 1350
while True:
    try:
        horas = float(input("Ingrese las horas trabajadas: "))
        if horas >= 0:
            sueldo = horas * sueldo_por_horas
            print(f"El sueldo a pagar es de ${sueldo} pesos. por la cantidad de {horas} horas trabajadas.")
        break
    except ValueError:
        print("Por favor, ingrese un número valido.")        
