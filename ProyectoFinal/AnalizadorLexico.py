import re
import tkinter as tk
from tkinter import filedialog, ttk
# Proyecto Final - Analizador Léxico para C#
#Integrantes: Ismenia Guevara, Sebastian Alzate, Jacobo Granada



# Definición de expresiones regulares para los tokens
# Se han agrupado los tokens por semántica para facilitar la lectura y el mantenimiento
token_specs = [
    # Comentarios
    ('COMENTARIO_BLOQUE',  r'/\*[\s\S]*?\*/'),
    ('COMENTARIO_LINEA',   r'//.*'),

    # Preprocesador
    ('PREPROCESADOR',   r'#(define|region|endregion|pragma)'),

    # Palabras clave específicas (agrupadas por semántica)
    ('CONDICIONAL',    r'\b(if|else|else\s+if)\b'),
    ('CICLO',          r'\b(for|while|do|foreach|break|continue)\b'),
    ('FLUJO',          r'\b(switch|case|default|goto)\b'),
    ('MANEJO_ERRORES', r'\b(try|catch|finally|throw)\b'),
    ('TIPO_DATO',      r'\b(int|float|double|bool|string|char|object|var|decimal|long|short|byte|sbyte|uint|ulong|ushort)\b'),
    ('KEYWORD',        r'\b(return|class|void|public|private|protected|static|using|namespace|new|this|base|const|readonly|dynamic)\b'),

    # Literales
    ('BOOL',           r'\b(true|false)\b'),
    ('NULL',           r'\bnull\b'),
    ('DOUBLE',         r'-?[0-9]+\.[0-9]+([eE][+-]?[0-9]+)?'),
    ('DECIMAL',        r'-?[0-9]+\.[0-9]+[mM]'),
    ('FLOAT',          r'-?[0-9]+\.[0-9]+[fF]?'),
    ('INT_NEGATIVO',   r'-[0-9]+'),
    ('INT_POSITIVO',   r'\b[0-9]+\b'),
    ('CADENA_TEXTO',         r'"([^"\\]|\\.)*"'),
    ('CARACTER',           r"'(\\.|[^\\'])'"),

    # Impresión
    ('IMPRIMIR', r'\b(System\.)?Console\.Write(Line)?\b'),

    # Identificadores
    ('IDENTIFICADOR',     r'\b[_a-zA-Z][_a-zA-Z0-9]*\b'),

    # Operadores
    ('OP_COMPARACION',      r'==|!=|<=|>=|<|>'),
    ('OP_LOGICO',           r'&&|\|\||!'),
    ('ASIGNACION',          r'=|\+=|\-=|\*=|/=|%='),
    ('OP_ARITMETICO',       r'\+|\-|\*|\/|%'),

    # Separadores
    ('SEPARADOR',      r'[;,.\[\]\(\)\{\}:]'),

    # Espacios (ignorados)
    ('ESPACIO_BLANCO',     r'\s+'),

    # Otros
    ('DESCONOCIDO',        r'.'),
]

# Compilación de la expresión regular
# Se utiliza un nombre de grupo para cada token para facilitar la identificación
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)


# Función para analizar el código y extraer los tokens
# Se ignoran los espacios en blanco
def lexer(code):
    tokens = []
    # Se utiliza re.finditer para encontrar todas las coincidencias de los tokens en el código
    for match in re.finditer(token_regex, code):
        # Se obtiene el nombre del grupo y el valor del token
        kind = match.lastgroup
        value = match.group()
        # Se ignoran los espacios en blanco
        if kind == 'ESPACIO_BLANCO':
            continue
        tokens.append((kind, value))
    return tokens


# GUI principal
# Se utiliza tkinter para crear una interfaz gráfica
# Se utiliza ttk para crear una tabla con los tokens
def mostrar_tokens_gui(tokens, archivo):
    root = tk.Tk()
    root.title("Analizador Léxico - Tokens")
    root.geometry("900x500")

    # Etiqueta
    label = tk.Label(root, text=f" Clasificación de Tokens ", font=("Arial", 12))
    label.pack(pady=10)

    # Tabla
    tree = ttk.Treeview(root, columns=("Tipo", "Valor"), show='headings')
    tree.heading("Tipo", text="Tipo de Token")
    tree.heading("Valor", text="Valor del Token")
    tree.column("Tipo", width=200)
    tree.column("Valor", width=580)

    # Colores por tipo
    style = ttk.Style()
    style.configure("Treeview", font=("Courier New", 10))
    style.map('Treeview', background=[('selected', '#444')])

    tag_colors = {
        'KEYWORD':     "#a4cdf5",
        'TIPO_DATO':   "#b5f4b5",
        'IMPRIMIR':   "#ffffb3",
        'IDENTIFICADOR':  "#e39af8",
        'INT_NEGATIVO':'#ffffff',
        'INT_POSITIVO':'#ffffff',
        'CADENA_TEXTO': '#ffffff',
        'CARACTER':    '#ffffff',
        'BOOL':        '#ffffff',
        'NULL':        '#ffffff',
        'OPERATOR':    '#ffffff',
        'OP_COMPARACION': '#ffffff',
        'OP_ARITMETICO': '#ffffff',
        'OP_LOGICO':   '#ffffff',
        'ASIGNACION':  '#ffffff',
        'SEPARADOR':   '#ffffff',
        'COMENTARIO_LINEA':'#ffffff',
        'COMENTARIO_BLOQUE':'#ffffff',
        'PREPROCESADOR':"#ffffff",
        'CONDICIONAL': "#ffffff",
        'CICLO':       "#ffffff",
        'FLUJO':       "#ffffff",
        'MANEJO_ERRORES': '#ffffff',
        'DESCONOCIDO':     "#fc4545",
        'DOUBLE':     "#ffffff",
        'DECIMAL':    "#ffffff",
        'FLOAT':      "#ffffff",
        'ESPACIO_BLANCO': "#ffffff",

    }

    # Se insertan los tokens en la tabla

    for token_type, value in tokens:
        tree.insert("", "end", values=(token_type, value), tags=(token_type,))
        if token_type in tag_colors:
            tree.tag_configure(token_type, background=tag_colors[token_type])

    tree.pack(expand=True, fill='both')

    # Botón para cerrar la ventana
    root.mainloop()



def main():
    tk.Tk().withdraw()  # Ocultar ventana principal
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo C#",
        filetypes=[("Archivos C#", "*.cs"), ("Todos los archivos", "*.*")]
    )

    if not file_path:
        print("No se seleccionó ningún archivo.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
            tokens = lexer(code)
            mostrar_tokens_gui(tokens, file_path)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
    main()