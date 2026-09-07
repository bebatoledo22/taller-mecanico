from vehiculo import Vehiculo # Importa la clase base Vehiculo

class Auto(Vehiculo): # Define la clase Auto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, cantidad_puertas: int): # Constructor con atributos heredados y propios
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo
        self.__cantidad_puertas: int = cantidad_puertas # Atributo privado con la cantidad de puertas

    def get_cantidad_puertas(self) -> int: # Getter para acceder a la cantidad de puertas de forma segura
        return self.__cantidad_puertas # Retorna el número de puertas

    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para aplicar tarifa de Auto
        return 6000 # Retorna el costo por hora para autos (por ejemplo $6000)
