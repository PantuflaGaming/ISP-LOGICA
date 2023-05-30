# E) Obtener la liquidacion  del sueldo de un empleado. La empresa bonifica sobre el sueldo basico (SB) la antiguedad del empleado con un 1.2% por año
# Además paga el presentismo en un monto fijo (MP).

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
hijos = int(input("¿Cuanto es la cantidad de hijos que posee: ")) #ln hijos
esposas = int(input("¿Cuanto es la cantidad de esposas que posee: ")) #ln esposas

# <=== Aberes ===>
presentismo = sueldoBasico * (8.33 / 100) #ln presentismo
antiguedad = (sueldoBasico * (1.2 / 100)) / 12 #ln antiguedad
salarioFamiliar = (30 * esposas) + (40 * hijos) #ln salarioFamiliar

# <=== Descuentos ===>

aporteJubilatorio = sueldoBasico * 0.11 #ln aporteJubilatorio
obraSocial = sueldoBasico * 0.3 #ln obraSocial
aporteGremial = sueldoBasico * 0.1 #ln aporteGremial

# <=== Estrategia ===>

totalLiquidar = (antiguedad + salarioFamiliar + sueldoBasico + presentismo) - (aporteJubilatorio + obraSocial + aporteGremial) #ln totalLiquidar

# <=== ESCRIBIR ===>
print("<=== DATOS ===> \n"
f" Empleado: {nombre}\n"
f"   DNI: {dni}\n"
 "\n" * 2,
f"Basico: {sueldoBasico}\n"
f"Antiguedad: {antiguedad}\n"
f"Presentismo: {presentismo}\n"
f"Salario Familiar {salarioFamiliar}\n"
 "\n" * 2,
 "Descuentos \n"
f"Aporte jubilatorio: {aporteJubilatorio}\n"
f"obra Social: {obraSocial}\n"
f"Aporte Gremial: {aporteGremial}\n"
"\n" * 2,
f"Liquido a cobrar: {totalLiquidar}"
)



# Fin programa