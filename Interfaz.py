# Calculadora de notas de estudiantes

# Paso 1: Captura de notas
notas = []
cantidad = int(input("¿Cuántas notas vas a ingresar? "))

for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

# Paso 2: Cálculo del promedio
promedio = sum(notas) / len(notas)

# Paso 3: Mostrar resultado
print("\n--- RESULTADO ---")
print(f"Notas ingresadas: {notas}")
print(f"Promedio final: {promedio:.2f}")

# Evaluación simple
if promedio >= 3.0:
    print("✅ ¡Aprobado!")
else:
    print("❌ Reprobado.")

