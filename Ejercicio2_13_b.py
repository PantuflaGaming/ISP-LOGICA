CostoKW = int(input("¿Cuanto vale el KW/h?: "))
MedidorAnterior = int(input("¿Cuanto fue la medida del periodo pasado?: "))
MedidorActual = int(input("¿Cuanto lleva gastado el medidor?: "))

ConsumoKW = MedidorAnterior - MedidorActual;
Costoconsumo = CostoKW * ConsumoKW
impuesto = Costoconsumo * 0,22;

print("El total a pagar es de: ", Costoconsumo + impuesto)