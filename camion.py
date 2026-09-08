from vehiculo import Vehiculo # Importa la clase base Vehiculo

class Camion(Vehiculo): # Define la clase Camion que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, capacidad_toneladas: float): # Constructor con atributos heredados y propios
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo
        self.set_capacidad_toneladas(capacidad_toneladas) # Asigna mediante el método setter con validación

    def get_capacidad_toneladas(self) -> float: # Getter para acceder a la capacidad de carga
        return self.__capacidad_toneladas # Retorna la capacidad en toneladas

    def set_capacidad_toneladas(self, capacidad_toneladas: float) -> None: # Setter con validación para la capacidad de carga
        if not isinstance(capacidad_toneladas, (int, float)) or isinstance(capacidad_toneladas, bool) or capacidad_toneladas <= 0: # Valida que sea número y mayor a 0
            raise ValueError(f"La capacidad de carga del camión ({capacidad_toneladas}) debe ser un número mayor a 0 toneladas.") # Lanza excepción si no es válida
        self.__capacidad_toneladas: float = float(capacidad_toneladas) # Asigna la capacidad validada al atributo privado

    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para aplicar tarifa de Camión
        return 10000 # Retorna el costo por hora para camiones (por ejemplo $10000)
