import pulp

# Crea un problema de maximización
problema = pulp.LpProblem("Maximizar_Utilidad", pulp.LpMaximize)

# Define las variables de decisión
x1 = pulp.LpVariable("X1", lowBound=0)
x2 = pulp.LpVariable("X2", lowBound=0)
x3 = pulp.LpVariable("X3", lowBound=0)

# Define la función objetivo
problema += 40 * x1 + 50 * x2 + 60 * x3, "Utilidad_Neta"

# Agrega las restricciones
problema += 4 * x1 + 4 * x2 + 5 * x3 <= 80, "Horas_de_Mano_de_Obra"
problema += 200 * x1 + 300 * x2 + 300 * x3 <= 6000, "Materia_Prima_R"
problema += 600 * x1 + 400 * x2 + 500 * x3 <= 5000, "Materia_Prima_S"

# Resuelve el problema
problema.solve()

# Imprime la solución
print("Status:", pulp.LpStatus[problema.status])
print("Cantidad óptima de X1 =", x1.varValue)
print("Cantidad óptima de X2 =", x2.varValue)
print("Cantidad óptima de X3 =", x3.varValue)
print("Valor óptimo de la función objetivo (utilidad neta) =", pulp.value(problema.objective))
