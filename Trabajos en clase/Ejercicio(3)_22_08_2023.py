# Un artesano vende el par de aros a $2 y las pulseras a $3 cada una. Pero tiene una
# oferta especial: vende un juego de un par de aros y una pulsera a $4. El sábado el
# artesano vendió: 72 pulseras, algunas en los juegos y otras sueltas y 80 pares de aros,
# algunos en los juegos y otros sueltos. El sábado vendió 52 juegos de oferta. ¿Cuánto
# dinero se llevó el artesano ese día por el total de las ventas?


#Establecemos precios

price_rings = int(input('Ingrese el valor de la unidad de los aros. \n'))
price_bracelet = int(input('Ingrese el valor de la unidad de las pulseras. \n'))
ofert = int(input('Ingrese el valor de la oferta tras comprar un par de aros y un par de pulseras. \n'))

input('Presiona enter para continuar.')
print('\n' * 20)

# Total de ventas
total_rings = int(input('Cuantos aros vendiste?'))
total_bracelets = int(input('Cuantas pulseras vendiste?'))
oferts = int(input('Cuantas ofertas vendiste?'))

total = (total_rings * price_rings) + (total_bracelets * price_bracelet) + ( oferts * ofert)

input('Presiona enter para continuar.')
print('\n' * 20)

print(f'Se logro obtener un total de ${total} entre todas las ventas.')