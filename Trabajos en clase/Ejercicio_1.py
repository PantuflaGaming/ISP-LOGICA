# Trabajo en clase

#Un comercio ofrece, solo por hoy, un descuento del 15% en todas las compras escriba un algoritmo que calcule el monto a pagar con el descuento.

# Datos: Descuento, montoaPagar
# Info: Calcular el descuento
# Estrategia: montoPagar - 0.15

montoPagar = int(input("Ingrese el monto total a pagar sin descuento: "))
descuento = montoPagar * 0.15;
montoFinal = montoPagar - descuento

print("El monto total a pagar con el descuento es:  ", montoFinal)