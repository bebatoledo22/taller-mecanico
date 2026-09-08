from vehiculo import Vehiculo # Importa la clase base Vehiculo

class Auto(Vehiculo): # Define la clase Auto que hereda de Vehiculo
    def __init__(self, patente: str, anio: int, cantidad_puertas: int): # Constructor con atributos heredados y propios
        super().__init__(patente, anio) # Llama al constructor de la clase padre Vehiculo
        self.set_cantidad_puertas(cantidad_puertas) # Asigna mediante el método setter con validación

    def get_cantidad_puertas(self) -> int: # Getter para acceder a la cantidad de puertas de forma segura
        return self.__cantidad_puertas # Retorna el número de puertas

    def set_cantidad_puertas(self, cantidad_puertas: int) -> None: # Setter con validación para la cantidad de puertas
        if not isinstance(cantidad_puertas, int) or isinstance(cantidad_puertas, bool) or cantidad_puertas < 2 or cantidad_puertas > 5: # Valida que sea entero entre 2 y 5
            raise ValueError(f"La cantidad de puertas ({cantidad_puertas}) debe ser un número entero entre 2 y 5.") # Lanza excepción si es inválido
        self.__cantidad_puertas: int = cantidad_puertas # Asigna el valor validado al atributo privado

    def tarifa_hora(self) -> int: # Sobrescribe el método tarifa_hora para aplicar tarifa de Auto
        return 6000 # Retorna el costo por hora para autos (por ejemplo $6000)
