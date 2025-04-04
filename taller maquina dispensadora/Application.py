import os  # Agregar esta importación

def leerArchivoAccsi(ruta):
    try:
        # Obtener la ruta absoluta basada en la ubicación del script
        ruta_absoluta = os.path.join(os.path.dirname(__file__), ruta)
        with open(ruta_absoluta, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe en la ruta: {ruta_absoluta}")
    except IOError:
        print("Error al leer el archivo")


def saludo_cliente():
        print("----------bienvenido a la maquina expendedora TLF------------")
        print("| primero ingrese las monedas de 1 pesos     | \n| necesarias para el producro que desea escoger| \n")
        #imgMaquina = leerArchivoAccsi('maquinaDibujo.txt')
        #imgMaquina = leerArchivoAccsi('asc.txt')
        #print(imgMaquina)

def verificarCredito(actual):
    moneda = "m"
    print("|+ presione [m] para meter monedas o [x] para terminar +|\npor favor ingrese 1 moneda")
    credito =0+actual
    while moneda == "m" or moneda == "x":
        moneda = input(":  ")
        if moneda == "m":
            credito+=1
            print("su credito es de: ", credito ,"$")
        else :
            if moneda == "x":
                return credito
    return credito

def comprarProducto(dinero,codigo):
    cambio=0
    precioProducto=0
    if codigo == "a":
        precioProducto = 2
    if codigo =="b":
        precioProducto=5
    if codigo=="c":
        precioProducto = 3
    if codigo=="d" :
        precioProducto =7
    if dinero-precioProducto >= 0:
        cambio = dinero-precioProducto
        print("!Compra exitosa¡")
        print("su cambio es : ", cambio , "$")
    else:
        print("dinero insuficiente")
def main():
    # saludamos al usuario y le presentamos una imagen accsi de bienvenida
    saludo_cliente()

    # verifiquemos que el usuario ingrese el credito suficiente
    print(leerArchivoAccsi('maquinaDibujo.txt'))
    creditos = verificarCredito(0)
    print("su saldo es ", creditos, "$")

    #realizar la compra
    #print(leerArchivoAccsi('asc.txt'))
    #print(leerArchivoAccsi('menu.txt'))
    print(f"---------- [ SELECIONE LA LETRA DEL PRODUCTO A COMPRAR, SALDO:  {creditos} $]  -------------")
    codigo = input(":  ")
    comprarProducto(creditos,codigo)

if __name__ == "__main__":
    main()
