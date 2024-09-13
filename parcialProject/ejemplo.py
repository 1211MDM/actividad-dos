#Conversión de tipos de datos (Enteros, Decimales y Cadenas)
#Convertir de entero a decimal
int_num = 15
decimal_num = float(int_num)
print(decimal_num)

#Convertir de decimal a entero
Valor = 5.59
integer = int(Valor)
print(integer)

#Convertir de cadena a decimal
string = "70.45"
decimal = float(string)
print(decimal)

#Convertir de cadena a entero
string = "80"
Valor = int(string)
print(Valor)

# Convertir entero a cadena
Valor = 15
string = str(Valor)
print(string)

# Convertir decimal a cadena
decimal = 1.25
string = str(decimal)
print(string)

#Multilíneas de cadenas.
name = "María del Mar"
multiline_string = f"texto\npara multiples lines\nHola, {name}!"
print(multiline_string)

#Función len().
my_string = "Hola, mundo!"
print(len(my_string))

#Sub cadenas:
def obtener_subcadena(cadena, inicio, fin):
  """
  Obtiene una subcadena de una cadena dada.

  Args:
    cadena: La cadena de la que se extraerá la subcadena.
    inicio: El índice inicial de la subcadena (incluido).
    fin: El índice final de la subcadena (excluido).

  Returns:
    La subcadena extraída.
  """
  return cadena[inicio:fin]

# Ejemplo de uso
cadena = "Esta es una cadena de ejemplo."
subcadena_inicio = obtener_subcadena(cadena, 0, 5)
subcadena_medio = obtener_subcadena(cadena, 5, 15)
subcadena_final = obtener_subcadena(cadena, 15, len(cadena))

print(f"Subcadena inicial: {subcadena_inicio}")
print(f"Subcadena del medio: {subcadena_medio}")
print(f"Subcadena final: {subcadena_final}")

#Función upper().
my_string = "Hola mundo"
print(my_string.upper())  # Output: "HELLO WORLD"

#Función lower()
# Ejemplo de uso de la función lower() en Python

# Ingreso de datos por el usuario
cadena = input("Ingrese una cadena de texto: ")

# Convertir la cadena a minúsculas
cadena_minusculas = cadena.lower()

# Mostrar el resultado
print("La cadena en minúsculas es:", cadena_minusculas)

# Multilíneas de cadenas de caracteres.
cadena_multilinea = """Esta es una cadena multilínea.
Se puede extender a varias líneas."""
print(cadena_multilinea)

# Función strip()
cadena_con_espacios = "  Hola Mundo  "
cadena_sin_espacios = cadena_con_espacios.strip()
print(cadena_sin_espacios)

# Función replace()
cadena_original = "Hola Mundo"
cadena_reemplazada = cadena_original.replace("Mundo", "Python")
print(cadena_reemplazada)

# Función split()
cadena_separada = "Hola,Mundo"
lista_palabras = cadena_separada.split(",")
print(lista_palabras)

# Formato de cadenas F-String.
nombre = "Chanel"
edad = 30
mensaje = f"Hola {nombre}, tienes {edad} años."
print(mensaje)














