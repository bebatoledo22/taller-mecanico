# Taller Mecánico

Repositorio para la asignatura de Programación Orientada a Objetos Seguro.

**Profesor:** Michael Arjel
**Institución:** Inacap

---

## Bitácora de Avances

### 25 de Agosto de 2026
- **Configuración Inicial:** Vinculación del directorio local con el repositorio de GitHub usando el CLI de GitHub (`gh auth`).
- **Limpieza:** Se eliminó la versión antigua del archivo `vehiculo.py` para construir el proyecto desde cero.
- **Clase Vehiculo (`vehiculo.py`):**
  - Se creó la clase principal del proyecto.
  - Se definieron los atributos privados `__patente`, `__anio` y `__en_taller` en el constructor, aplicando encapsulamiento y *type hints*.
  - Se crearon los métodos `ingresar()` y `entregar()` con validación de estado.
  - Se creó el método `tarifa_hora()` que retorna un valor fijo de 5000.
- **Script de Pruebas (`main.py`):**
  - Se creó el archivo de ejecución principal.
  - Se importó la clase `Vehiculo` y se instanciaron 3 objetos con datos ficticios.
  - Se probó la invocación de métodos y la impresión de la tarifa por hora en consola.
- **Documentación:** Se comentaron todas las líneas de código en ambos archivos (`vehiculo.py` y `main.py`) explicando paso a paso su funcionamiento con fines educativos.

### 8 de Septiembre de 2026
- **Validaciones en Subclases (`auto.py` y `camion.py`):**
  - En `Auto`: validación de cantidad de puertas (entero entre 2 y 5) lanzando `ValueError`.
  - En `Camion`: validación de capacidad de carga (número mayor a 0 toneladas) lanzando `ValueError`.
- **Manejo de Excepciones (`main.py`):**
  - Implementación de bloques `try ... except` para proteger el flujo del programa ante datos no válidos.
  - Pruebas de captura de excepciones para patentes con formato incorrecto, años fuera de rango, capacidades de carga negativas y cantidades de puertas inválidas.
- **Mantenimiento:** Se removieron del control de versiones los archivos de caché (`__pycache__`) respetando `.gitignore`.

