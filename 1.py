class Persona:
    """
    Clase para representar una persona.
    Atributos:
        - nombre: str (opcional)
        - edad: int (opcional)
        - dni: str (opcional)
    Métodos:
        - mostrar: Muestra los datos de la persona.
        - esMayorDeEdad: Devuelve True si la persona es mayor de edad, False en caso contrario.
    """

    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Getters y setters con validación
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__nombre = valor
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self.__edad = valor
        else:
            raise ValueError("La edad debe ser un entero no negativo.")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__dni = valor
        else:
            raise ValueError("El DNI debe ser una cadena no vacía.")

    def mostrar(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__dni}"

    def esMayorDeEdad(self):
        return self.__edad >= 18


# Prueba del programa
persona = Persona("Juan", 20, "12345678X")
print(persona.mostrar())
print(f"¿Es mayor de edad? {persona.esMayorDeEdad()}")