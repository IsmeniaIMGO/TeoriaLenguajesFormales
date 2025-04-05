import os
#Materia: Teoria de Lenguajes Formales

# Taller de programación: Máquina dispensadora

#Estudiantes:
# Ismenia Marcela Guevara Ortiz
# Jhon Sebastian Alzate Andica


class MaquinaDispensadora:

    #
    def __init__(self):

        self.credito = 0
        # Definición de productos y precios
        self.productos = {
            "A": {"nombre": "Snack", "precio": 2},
            "B": {"nombre": "Bebida", "precio": 5},
            "C": {"nombre": "Dulce", "precio": 3},
            "D": {"nombre": "Café", "precio": 7},
        }


    # Método para mostrar el menú de la máquina
    def mostrar_menu(self):
        print(self.leer_archivo("maquinaDibujo.txt"))


    # Método para leer el archivo de texto
    def leer_archivo(self,ruta):
        try:
            ruta_absoluta = os.path.join(os.path.dirname(__file__), ruta)
            with open(ruta_absoluta, 'r') as archivo:
                return archivo.read()
        except FileNotFoundError:
            return f"El archivo '{ruta}' no existe."
        except IOError:
            return "Error al leer el archivo."


    # Método para ingresar monedas
    def ingresar_monedas(self):
        print("| Presione [+] para meter monedas |")
        while True:
            moneda = input(": ")
            if moneda == "+":
                self.credito += 1
                print(f"Su crédito es de: {self.credito} $")
            else:
                break


    # Método para seleccionar un producto
    def seleccionar_producto(self):
        print(f"\n| SELECCIONE LA LETRA DEL PRODUCTO A COMPRAR, SALDO: {self.credito} $ |")
        codigo = input(": ").upper()
        if codigo in self.productos:
            return codigo
        else:
            print("Código inválido. Intente nuevamente.")
            return self.seleccionar_producto()

    # Método para comprar un producto
    def comprar_producto(self, codigo):
        producto = self.productos[codigo]
        precio = producto["precio"]
        if self.credito >= precio:
            self.credito -= precio
            print(f"¡Compra exitosa! Ha comprado {producto['nombre']}.")
            print(f"Su cambio es: {self.credito} $")
            self.credito = 0  # Reiniciar el crédito después de la compra
        else:
            print("Dinero insuficiente. Por favor, ingrese más monedas.")


    def iniciar(self):
        self.mostrar_menu()
        print("\n| Primero ingrese las monedas necesarias para el producto que desea escoger |")
        self.ingresar_monedas()
        codigo = self.seleccionar_producto()
        self.comprar_producto(codigo)


# Ejecución del programa
if __name__ == "__main__":
    maquina = MaquinaDispensadora()
    maquina.iniciar()