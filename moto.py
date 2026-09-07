from datetime import datetime # Importa datetime para obtener el año actual dinámicamente
from vehiculo import Vehiculo # Importa la clase base Vehiculo

class Moto(Vehiculo): # Define la clase Moto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, cilindrada: int): # Constructor con atributos heredados y propios
        self.validar_anio(anio) # Valida el año del modelo antes de inicializar el objeto
        super().__init__(patente, anio) # Llama al constructor de la clase base Vehiculo
        self.__cilindrada: int = cilindrada # Atributo privado con la cilindrada en centímetros cúbicos (cc)

    @staticmethod
    def validar_anio(anio: int) -> int: # Método para validar los años del modelo de la moto
        anio_actual = datetime.now().year # Obtiene el año en curso
        anio_minimo = 1900 # Define el año mínimo válido para un modelo de moto
        anio_maximo = anio_actual + 1 # Permite modelos hasta el año siguiente (nuevos lanzamientos)

        if not isinstance(anio, int) or isinstance(anio, bool): # Valida que el año sea un entero
            raise ValueError("El año del modelo de la moto debe ser un número entero.")

        if anio < anio_minimo or anio > anio_maximo: # Valida que se encuentre dentro del rango válido
            raise ValueError(f"El año del modelo de la moto ({anio}) debe estar entre {anio_minimo} y {anio_maximo}.")

        return anio # Retorna el año validado

    def get_cilindrada(self) -> int: # Getter para acceder a la cilindrada
        return self.__cilindrada # Retorna los centímetros cúbicos (cc)

    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para aplicar tarifa de Moto
        return 3500 # Retorna el costo por hora para motos (por ejemplo $3500)
