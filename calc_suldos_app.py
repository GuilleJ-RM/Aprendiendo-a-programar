sueldo_por_horas = 1350
while True:
    try:
        horas = input("Ingrese las horas trabajadas o '0' para salir: ")
        if horas == "0" :
            print("Gracias por usar la calculadora de sueldos.")
        else:
            horas = float(horas)
            sueldo = horas * sueldo_por_horas
            print(f"El sueldo a pagar es de ${sueldo: .2f} pesos. por la cantidad de {horas: .2f} horas trabajadas.")
        break
    except ValueError:
        print("Por favor, ingrese un número valido.")
