# Realizar un algoritmo que imprima el mínimo de cuatro valores que se piden al usuario.

valor1 = int(input('Ingrese el primer valor: '))
valor2 = int(input('Ingrese el segundo valor: '))
valor3 = int(input('Ingrese el tercer valor: '))
valor4 = int(input('Ingrese el cuarto valor: '))
menor = 0;

if valor2 < valor1 and valor2 < valor3 and valor2 < valor4:
    print("El menor es el segundo valor: ", valor2);
elif valor3 < valor1 and valor3 < valor4:
    print("El menor es el tercer valor: ", valor3);
elif valor4 < valor1:
    print("El menor es el cuarto valor: ", valor4);
else:
    print("El menor es el primer valor: ", valor1);