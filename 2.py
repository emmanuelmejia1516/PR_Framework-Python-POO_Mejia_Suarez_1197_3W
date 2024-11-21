class Persona:
    """
    Clase para representar una persona.
    """
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

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


class Cuenta:
    """
    Clase para representar una cuenta bancaria.
    """
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = float(cantidad)

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        if isinstance(valor, Persona):
            self.__titular = valor
        else:
            raise ValueError("El titular debe ser una instancia de la clase Persona.")

    @property
    def cantidad(self):
        return self.__cantidad

    def mostrar(self):
        return f"Titular: {self.titular.mostrar()}, Cantidad: {self.__cantidad:.2f}"

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


# Prueba del programa
persona = Persona("María", 25, "87654321Z")
cuenta = Cuenta(persona, 100.0)
cuenta.ingresar(50)
cuenta.retirar(30)
print(cuenta.mostrar())