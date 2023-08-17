import math

# E) Obtener la liquidacion  del sueldo de un empleado. La empresa bonifica sobre el sueldo basico (SB) la antiguedad del empleado con un 1.2% por año
# Además paga el presentismo en un monto fijo (MP). Entre los descuentos, aporte jubilatorio con un 11% del sueldo basico, Obra social con un 3% del basico
# y el aporte gremial con 1% del basico. Además, el empleador paga $40.00 por hijo y por esposa $30.00.

# INFO: Calcular la liquidacion del sueldo
# Datos: Haberes - Sueldo Basico, 1.2%, MP, 30.00 y 40.00
# Descuentos - Jubilatrio 11% , Obra Social 3%,  Aporte Gremial1%
# Estrategia: Haberes - Descuento.
#================================================================================
#Programa Liquidacion de sueldo

# <=== LEER ===>
nombre = str(input("¿Cual es su nombre?: "))  # ls Nombre
dni = int(input("¿Cual es tu DNI?: ")) #ln dni
sueldoBasico = int(input("¿Cuando es el sueldo basico?: ")) #ln sueldoBasico
anosAntiguedad = int(input("¿Cuantos años tiene de antiguedad?: "))
hijos = int(input("¿Cuanto es la cantidad de hijos que posee: ")) #ln hijos
esposas = int(input("Ingrese [1 si posee esposa y [0] si no posee esposa: ")) #ln esposas

# <=== haberes ===>
presentismo = sueldoBasico * (8.33 / 100) #ln presentismo
antiguedad = (sueldoBasico * (1.2 / 100) * anosAntiguedad#ln antiguedad
salarioFamiliar = (30 * esposas) + (40 * hijos) #ln salarioFamiliar

# <=== Descuentos ===>

aporteJubilatorio = sueldoBasico * 0.11 #ln aporteJubilatorio
obraSocial = sueldoBasico * 0.03 #ln obraSocial
aporteGremial = sueldoBasico * 0.01 #ln aporteGremial

# <=== Estrategia ===>

totalLiquidar = (antiguedad + salarioFamiliar + sueldoBasico + presentismo) - (aporteJubilatorio + obraSocial + aporteGremial) #ln totalLiquidar

# <=== ESCRIBIR ===>
print('\n' * 10)
print("<=== DATOS ===> \n"
f" Empleado: {nombre}\n"
f"  DNI: {dni}\n"
 "\n" * 2,
f"Haberes \n"
f"  Sueldo Basico: {sueldoBasico}\n"
f"  Antiguedad: {antiguedad}\n"
f"  Presentismo: {presentismo}\n"
f"  Salario Familiar {salarioFamiliar}\n"
 "\n" * 2,
 "Descuentos \n"
f"  Aporte jubilatorio: {aporteJubilatorio}\n"
f"  obra Social: {obraSocial}\n"
f"  Aporte Gremial: {aporteGremial}\n"
"\n" * 2,
f"  Liquido a cobrar: {totalLiquidar}"
)



# Fin programa
