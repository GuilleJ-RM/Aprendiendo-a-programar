 #Calcular el importe que debe pagar una persona que compra una heladera de pesos
#X y por pagar en efectivo le hacen el 10% de descuento, ¿cuánto abona?
precio_original = float(input("Ingrese el precio original de la heladera: "))
descuento = precio_original * 0.10
precio_final = precio_original - descuento
print(f"El precio original de la heladera es de ${precio_original: .2f} pesos.")