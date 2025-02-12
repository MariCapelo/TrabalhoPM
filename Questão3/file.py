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
print("Item A: ")
print(f"Valor de x1: {value(x1)}")
print(f"Valor de x2: {value(x2)}")
print(f"Máximo de Lucro: {value(Z.objective)}")
print("-"*40)

# Item B) 
print("Item B: ")
for nome, restricao in Z.constraints.items():
    print(f"{nome}: Preço Dual = {restricao.pi}")
print("-"*40)

#Item C)
print("Item C: \n")
Z.constraints["Limite_Mercado1"] = x1 <= 120
Z.solve()
print(f"Máximo de Lucro: {value(Z.objective)}")
print("-"*40)

#Item D)
print("Item D")
preco_dual_limite_mercado2 = Z.constraints["Limite_Mercado2"].pi
aumento_limite_mercado2 = 10
efeito_aumento_receita_otima = aumento_limite_mercado2 * preco_dual_limite_mercado2
print(f"Efeito sobre a receita ótima ao aumentar a participação de mercado do chapéu do tipo 2 em {aumento_limite_mercado2} unidades: {efeito_aumento_receita_otima}")
print("-"*40)