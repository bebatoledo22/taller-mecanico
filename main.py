from auto import Auto # Importa la subclase Auto
from camion import Camion # Importa la subclase Camion
from moto import Moto # Importa la subclase Moto

# Instanciación de objetos de cada tipo de vehículo
auto1 = Auto("AB1234", 2020, 4) # Auto con patente, año y 4 puertas
camion1 = Camion("CD5678", 2018, 12.5) # Camión con patente, año y capacidad de 12.5 toneladas
moto1 = Moto("EF9012", 2023, 250) # Moto con patente, año y 250 cc

# Registro de ingreso al taller
print(auto1.ingresar()) # Ingreso del auto
print(camion1.ingresar()) # Ingreso del camión
print(moto1.ingresar()) # Ingreso de la moto

# Impresión de tarifas diferenciadas y atributos propios
print(f"Tarifa Auto ({auto1.get_cantidad_puertas()} puertas): ${auto1.tarifa_hora()}/hora")
print(f"Tarifa Camión ({camion1.get_capacidad_toneladas()} toneladas): ${camion1.tarifa_hora()}/hora")
print(f"Tarifa Moto ({moto1.get_cilindrada()} cc): ${moto1.tarifa_hora()}/hora")
