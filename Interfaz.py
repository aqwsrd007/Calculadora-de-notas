if cantidad > 0:
2
promedio = sum(notas) / len(notas)
3
 
4
print("\n--- RESULTADO ---")
5
print(f"Notas ingresadas: {notas}")
6
print(f"Promedio final: {promedio:.2f}")
7
 
8
if promedio >= 3.0:
9
print("✅ ¡Aprobado!")
10
else:
11
print("❌ Reprobado.")
12
else:
13
print("Debes ingresar al menos una nota.")
14
``
Mostrar más líneas

Si al ejecutarlo en GitHub Codespaces o VS Code te aparece un mensaje de error, compárteme el error exacto y te digo cómo corregirlo.

Proporcione sus comentarios sobre BizChat
You said:
muestrame el codigo corregido
Copilot said:

Aquí tienes el código corregido y mejorado para evitar errores si el usuario ingresa 0 notas:

Python
1
# Calculadora de notas de estudiantes
2
 
3
# Paso 1: Captura de notas
4
notas = []
5
cantidad = int(input("¿Cuántas notas vas a ingresar? "))
6
 
7
if cantidad > 0:
8
for i in range(cantidad):
9
nota = float(input(f"Ingrese la nota {i + 1}: "))
10
notas.append(nota)
11
 
12
# Paso 2: Cálculo del promedio
13
promedio = sum(notas) / len(notas)
14
 
15
# Paso 3: Mostrar resultado
16
print("\n--- RESULTADO ---")
17
print(f"Notas ingresadas: {notas}")
18
print(f"Promedio final: {promedio:.2f}")
19
 
20
# Evaluación simple
21
if promedio >= 3.0:
22
print("✅ ¡Aprobado!")
23
else:
24
print("❌ Reprobado.")
25
else:
26
print("⚠️ Debes ingresar al menos una nota.")
