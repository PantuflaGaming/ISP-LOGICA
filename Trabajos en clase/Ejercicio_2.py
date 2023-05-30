# # Segundo Ejercicio
# Escriba un algoritmo que lea 4 notas de un estudiante y cacule el promedio de las mismas
# Info: Calcular el promedio de las 4 notas
# Datos: Notas
# Estrategia: Notas / cantidad

nota1 = int(input("¿Cuanto fue la primera nota final?: "))
nota2 = int(input("¿Cuanto fue la segunda nota final?: "))
nota3 = int(input("¿Cuanto fue la tercera nota final?: "))
nota4 = int(input("¿Cuanto fue la cuarta nota final?: "))

promedio = (nota1+nota2+nota3+nota4) / 4;

print("El promedio total entre las 4 materias es: ", promedio)