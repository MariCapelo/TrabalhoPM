from pulp import *

# Definir o problema
Z = LpProblem("Chapeus_Wild_West", LpMaximize)

# Definir as variáveis
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)

# Definir a função objetivo
Z += 8 * x1 + 5 * x2, "Lucro"

# Definir as restrições
Z += (2*x1 + x2 <= 400, "Mao-de-Obra")
Z += (x1 <= 150, "Limite_Mercado1")
Z += (x2 <= 200, "Limite_Mercado2")

# Resolver o problema
Z.solve()

# Item A)
print(f"Valor de x1: {value(x1)}")
print(f"Valor de x2: {value(x2)}")
print(f"Máximo de Lucro: {value(Z.objective)}")

# Item B)
for nome, restricao in Z.constraints.items():
    print(f"{nome}: Preço Dual = {restricao.pi}")