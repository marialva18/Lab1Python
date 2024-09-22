# Problema 1
nombre = input("Introduce tu nombre: ")
print(f"¡Hola {nombre}!")

# Problema 2
consumo = float(input("Introduce el total del consumo: "))
porcentaje = float(input("Introduce el porcentaje de propina: "))
propina = consumo * (porcentaje / 100)
print(f"La propina es: {propina}")

# Problema 3
payasos = int(input("Introduce el número de payasos vendidos: "))
munecas = int(input("Introduce el número de muñecas vendidas: "))
peso_total = (payasos * 112) + (munecas * 75)
print(f"El peso total del paquete es: {peso_total} gramos")

# Problema 4
N = int(input("Introduce un número entero positivo: "))
suma_total = sum(range(1, N + 1))
print(f"La suma de los primeros {N} enteros es: {suma_total}")

# Problema 5
shows = int(input("¿Cuántos shows musicales viste en el último año? "))
print(shows > 3)

# Problema 6
edad = int(input("Introduce tu edad: "))
if edad < 4:
    print("Entrada gratis")
elif 4 <= edad <= 18:
    print("El precio de la entrada es $5")
else:
    print("El precio de la entrada es $10")

# Problema 7
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
print("1. Sumar\n2. Restar\n3. Multiplicar")
opcion = int(input("Elige una opción: "))
if opcion == 1:
    print(f"Resultado: {num1 + num2}")
elif opcion == 2:
    print(f"Resultado: {num1 - num2}")
elif opcion == 3:
    print(f"Resultado: {num1 * num2}")
else:
    print("Opción inválida")

# Problema 8
hora = input("Introduce la hora en formato 24 horas (HH:MM): ")
horas, minutos = map(int, hora.split(":"))
hora_decimal = horas + minutos / 60
if 7 <= hora_decimal <= 8:
    print("Es hora de desayunar")
elif 12 <= hora_decimal <= 13:
    print("Es hora de almorzar")
elif 18 <= hora_decimal <= 19:
    print("Es hora de cenar")

# Problema 9
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = lista_original[::-1]
print(lista_invertida)

# Problema 10
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
lista_muestra = [x for i, x in enumerate(lista_muestra) if i not in [0, 4, 5]]
print(lista_muestra)

# Problema 11
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_sin_duplicados = list(set(lista_original))
print(lista_sin_duplicados)

# Problema 12
archivo = input("Introduce el nombre del archivo: ")
extensiones_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}
extension = archivo[archivo.rfind("."):].lower()
tipo_mime = extensiones_mime.get(extension, "application/octet-stream")
print(tipo_mime)
