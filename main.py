from auto import Auto # Importa la subclase Auto
from camion import Camion # Importa la subclase Camion
from moto import Moto # Importa la subclase Moto

# Instanciación de objetos dentro de un bloque try-except para manejo seguro
print("--- 1. Instanciación y flujo con datos correctos ---")
try:
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

except ValueError as error: # Captura cualquier excepción de validación lanzada por los objetos
    print(f"Error durante la creación: {error}") # Informa el error capturado

print("\n--- 2. Pruebas de captura de excepciones con datos erróneos ---")

# Prueba 1: Patente inválida (menos de 6 caracteres y con espacio)
try:
    print("Intentando crear un auto con patente inválida...")
    auto_invalido = Auto("A 12", 2022, 2) # Patente incorrecta que activará el raise ValueError
except ValueError as error: # Captura la excepción lanzada por la validación del setter de patente
    print(f"Excepción capturada con éxito: {error}") # Muestra el mensaje sin detener el programa

# Prueba 2: Año fuera de rango para Moto
try:
    print("\nIntentando crear una moto con año no permitido...")
    moto_invalida = Moto("GH3456", 1850, 150) # Año 1850 fuera del rango permitido (>= 1900)
except ValueError as error: # Captura la excepción lanzada por validar_anio de Moto
    print(f"Excepción capturada con éxito: {error}") # Muestra el mensaje sin detener el programa

# Prueba 3: Capacidad de carga no permitida en Camión (<= 0)
try:
    print("\nIntentando crear un camión con capacidad negativa o cero...")
    camion_invalido = Camion("IJ7890", 2019, -5.0) # Capacidad negativa que activará el raise ValueError
except ValueError as error: # Captura la excepción lanzada por set_capacidad_toneladas de Camion
    print(f"Excepción capturada con éxito: {error}") # Muestra el mensaje sin detener el programa

# Prueba 4: Cantidad de puertas inválida en Auto (fuera del rango 2 a 5)
try:
    print("\nIntentando crear un auto con 8 puertas...")
    auto_puertas_invalidas = Auto("KL1234", 2021, 8) # 8 puertas excede el rango permitido de 2 a 5
except ValueError as error: # Captura la excepción lanzada por set_cantidad_puertas de Auto
    print(f"Excepción capturada con éxito: {error}") # Muestra el mensaje sin detener el programa


