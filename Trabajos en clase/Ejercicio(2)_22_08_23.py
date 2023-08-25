# Juan compró un lote en la Antártida y se está construyendo un iglú. La base del mismo
# es circular. Los bloques que consigue para armar la pared perimetral de dicho círculo
# tienen 36 cm de largo. Sabe que el diámetro de dicho círculo es de 8 mt. Cuántos
# ladrillos necesita para la primera hilera?
# O - 36cm - 8mts 0.36mts

import math

# Solicitamos que ingrese el diametro de la circunferencia y el largo o tama;o de los ladrillos. 

diameter = int(input('Ingrese la cantidad de diametros que contiene el iglu en metros. \n'))
brick_size = float(input('Ingrese el largo del ladrillo en metros. \n'))
r = diameter / 2

# Calculamos cuanto mide la circuferencia   
c = 2 * math.pi * r

# Pasamos a centimetros la circuferencia y los bricke_size
c_centimeters = c * 100
brick_centimeters = brick_size * 100

# Calculamos la cantidad de ladrillos que necesitara en la primera ilera
bricks_needs = round(c_centimeters/brick_centimeters)

# Mostramos en pantalla el resultado
print(f'Necesitaras un total de {bricks_needs} ladrillos para realizar la primera hilera de la pared perimetral.') 
