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


class CuentaJoven(Cuenta):
    """
    Clase que representa una cuenta joven derivada de la clase Cuenta.
    """
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, valor):
        if isinstance(valor, (int, float)) and 0 <= valor <= 100:
            self.__bonificacion = valor
        else:
            raise ValueError("La bonificación debe ser un porcentaje entre 0 y 100.")

    def esTitularValido(self):
        return self.titular.edad >= 18 and self.titular.edad < 25

    def mostrar(self):
        return f"Cuenta Joven\nTitular: {self.titular.mostrar()}\nCantidad: {self.cantidad:.2f}\nBonificación: {self.__bonificacion}%"

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            raise PermissionError("El titular no es válido para retirar dinero.")


# Prueba del programa
persona_joven = Persona("Luis", 22, "12345678Y")
cuenta_joven = CuentaJoven(persona_joven, 200.0, 10)
print(cuenta_joven.mostrar())
cuenta_joven.retirar(50)
print(cuenta_joven.mostrar())