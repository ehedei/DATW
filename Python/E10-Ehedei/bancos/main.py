from plazo_fijo import *
from caja_ahorro import *

caja = CajaAhorro('Ehedei', 9534.71)
caja.mostrar_datos()

print('-------------------------')

plazo = PlazoFijo('Estanislaski I de Cuba', 13253.10, 36, 8)
plazo.mostrar_datos()
print('El interés de la cuenta a Plazo Fijo es de ', str(plazo.calcular_interes()))