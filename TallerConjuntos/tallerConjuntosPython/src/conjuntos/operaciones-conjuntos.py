""" 
    Integrantes: Bryan Gómez Marín - Ismenia Marcela Guevara Ortiz

    Implementación de las operaciones de conjuntos
    - Unión
    - Intersección
    - Diferencia
    - Diferencia simétrica
    - Subconjunto
    - Superconjunto
    - Propiedades de conjuntos
"""




class Conjunto:

    # inicializa un conjunto eliminando duplicados de la lista de elementos proporcionada.
    def __init__(self, elementos):
        self.elementos = []
        for e in elementos:
            if e not in self.elementos:
                self.elementos.append(e)
        self.elementos.sort()

    """
    toma una lista de conjuntos y devuelve un nuevo conjunto
    que contiene todos los elementos únicos de los conjuntos involucrados.
    """
    def union(self, conjuntos):
        resultado = self.elementos[:]
        for conjunto in conjuntos:
            for elemento in conjunto.elementos:
                if elemento not in resultado:
                    resultado.append(elemento)
        return Conjunto(resultado)


    """
    devuelve un nuevo conjunto con los elementos comunes
    a todos los conjuntos proporcionados.
    """
    def interseccion(self, conjuntos):
        resultado = self.elementos[:]
        for conjunto in conjuntos:
            resultado = [e for e in resultado if e in conjunto.elementos]
        return Conjunto(resultado)


    """
    devuelve un nuevo conjunto con los elementos que 
    están en el conjunto actual pero no en el otro conjunto proporcionado
    """
    def diferencia(self, otro):
        resultado = [e for e in self.elementos if e not in otro.elementos]
        return Conjunto(resultado)


    """
    combina las diferencias de ambos conjuntos para 
    devolver un conjunto con los elementos que están en uno u otro conjunto, pero no en ambos.
    """
    def diferencia_simetrica(self, otro):
        diferencia1 = self.diferencia(otro).elementos
        diferencia2 = otro.diferencia(self).elementos
        return Conjunto(diferencia1 + diferencia2)


    """
    Un conjunto A es un subconjunto de otro conjunto B
    si todos los elementos de A están en B.
    """
    def es_subconjunto(self, otro):
        for e in self.elementos:
            if e not in otro.elementos:
                return False
        return True


    """
    Un conjunto B es un superconjunto de otro conjunto A 
    si B contiene todos los elementos de A.
    """
    def es_superconjunto(self, otro):
        return otro.es_subconjunto(self)


    """
    proporciona una representación en cadena del conjunto, 
    formateada como una lista de elementos entre llaves.
    """
    def representacion(self):
        return "{" + ", ".join(map(str, self.elementos)) + "}"



    """
    verifica varias propiedades de los conjuntos, 
    como la conmutatividad de la unión e intersección, 
    la asociatividad, y las leyes de absorción. 
    Este método devuelve una cadena con los resultados de estas verificaciones.
    """

    
    def propiedades(self, segundo, tercero):

        print("\n" + "Propiedades de conjuntos:")

        union1 = self.union([segundo])
        union2 = segundo.union([self])
        interseccion1 = self.interseccion([segundo])
        interseccion2 = segundo.interseccion([self])
        union_asociativa1 = self.union([segundo]).union([tercero])
        union_asociativa2 = self.union([segundo.union([tercero])])
        interseccion_asociativa1 = self.interseccion([segundo]).interseccion([tercero])
        interseccion_asociativa2 = self.interseccion([segundo.interseccion([tercero])])
        union_distributiva1 = self.union([segundo.interseccion([tercero])])
        union_distributiva2 = self.union([segundo]).interseccion([self.union([tercero])])
        union_idempotente = self.union([self])
        interseccion_idempotente = self.interseccion([self])

        print("A ∪ B:", union1.representacion())
        print("B ∪ A:", union2.representacion())
        print("A ∩ B:", interseccion1.representacion())
        print("B ∩ A:", interseccion2.representacion())
        print("(A ∪ B) ∪ C:", union_asociativa1.representacion())
        print("A ∪ (B ∪ C):", union_asociativa2.representacion())
        print("(A ∩ B) ∩ C:", interseccion_asociativa1.representacion())
        print("A ∩ (B ∩ C):", interseccion_asociativa2.representacion())
        print("A ∪ (B ∩ C):", union_distributiva1.representacion())
        print("(A ∪ B) ∩ (A ∪ C):", union_distributiva2.representacion())
        print("A ∪ A:", union_idempotente.representacion())
        print("A ∩ A:", interseccion_idempotente.representacion())


        return "\n".join([
        "A ∪ B = B ∪ A: " + str(union1.elementos == union2.elementos),
        "A ∩ B = B ∩ A: " + str(interseccion1.elementos == interseccion2.elementos),
        "(A ∪ B) ∪ C = A ∪ (B ∪ C): " + str(union_asociativa1.elementos == union_asociativa2.elementos),
        "(A ∩ B) ∩ C = A ∩ (B ∩ C): " + str(interseccion_asociativa1.elementos == interseccion_asociativa2.elementos),
        "A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C): " + str(union_distributiva1.elementos == union_distributiva2.elementos),
        "A ∪ A = A, A ∩ A = A: " + str(union_idempotente.elementos == self.elementos and interseccion_idempotente.elementos == self.elementos)
    ])
    


# Solicitar al usuario que ingrese los elementos de los conjuntos
def ingresar_conjunto(nombre):
    elementos = []
    print(f"Ingrese los elementos del conjunto {nombre} uno por uno. Escriba 'fin' para terminar y \ncontinuar con el siguiente conjunto:")
    while True:
        elemento = input("Elemento: ")
        if elemento.lower() == 'fin':
            break
        elementos.append(elemento)
    return Conjunto(elementos)

# Ejemplo de uso:
A = ingresar_conjunto("A")
B = ingresar_conjunto("B")
C = ingresar_conjunto("C")


print("\nConjuntos:")
print("Conjunto A:", A.representacion())
print("Conjunto B:", B.representacion())
print("Conjunto C:", C.representacion() + "\n")
print("Unión A ∪ B = ", A.union([B]).representacion() + "\n")
print("Intersección A ∩ B = ", A.interseccion([B]).representacion() + "\n")
print("Diferencia A - B = ", A.diferencia(B).representacion() + "\n")
print("Diferencia Simétrica A Δ B = ", A.diferencia_simetrica(B).representacion() + "\n")
print("Subconjunto A ⊂ B = ", A.es_subconjunto(B))
print("")
print("Superconjunto B ⊃ A = ", B.es_superconjunto(A))
print("\nPropiedades:\n" + A.propiedades(B, C))

