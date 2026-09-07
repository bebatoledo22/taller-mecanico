from vehiculo import Vehiculo # Importa la clase base Vehiculo

class Moto(Vehiculo): # Define la clase Moto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, cilindrada: int): # Constructor con atributos heredados y propios
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo
        self.__cilindrada: int = cilindrada # Atributo privado con la cilindrada en centímetros cúbicos (cc)

    def get_cilindrada(self) -> int: # Getter para acceder a la cilindrada
        return self.__cilindrada # Retorna los centímetros cúbicos (cc)

    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para aplicar tarifa de Moto
        return 3500 # Retorna el costo por hora para motos (por ejemplo $3500)
