from vehiculo import Vehiculo # Importa la clase base Vehiculo

class Camion(Vehiculo): # Define la clase Camion que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_toneladas: float): # Constructor con atributos heredados y propios
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo
        self.__capacidad_toneladas: float = capacidad_toneladas # Atributo privado con la capacidad de carga en toneladas

    def get_capacidad_toneladas(self) -> float: # Getter para acceder a la capacidad de carga
        return self.__capacidad_toneladas # Retorna la capacidad en toneladas

    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para aplicar tarifa de Camión
        return 10000 # Retorna el costo por hora para camiones (por ejemplo $10000)
