from pulp import *

# Definição do problema 
Z = LpProblem("Maximo_De_Lucro", LpMaximize)

#Criando as variaveis do problema
# carteira = x1 / estojo = x2 / mochila = x3 
x1 = LpVariable("x1", lowBound = 1)
x2 = LpVariable("x2", lowBound = 1)
x3 = LpVariable("x3", lowBound = 1)

#Função Objetivo
Z += 24*x1 + 22*x2 + 45*x3

#Definir as Restrições 
Z += 2*x1 + x2 + 3*x3 <= 42
Z += 2*x1 + x2 + 2*x3 <= 40
Z += x1 + 0.5*x2 + x3 <= 45

# A função variable.solve() irá retornar um bolleano indicando se há ou não  
# uma solução otima para o problema apresntado.
if Z.solve():
    print("Existe uma solução ótima!\n")
    print("Item A)")
    for v in Z.variables():
        print(v.name, " = ", v.varValue)
    print("Valor máximo de lucro: ", value(Z.objective))
    print("\nItem B)")
    couro = value(2*x1 + x2 + 3*x3)
    costura = value(2*x1 + x2 + 2*x3)
    acabamento = value(x1 + 0.5*x2 + x3)
    print("Quantidade de cada recurso utilizado na solução otima: ")
    print("Couro = ", couro)
    print("Costura = ", costura)
    print("Acabamento = ", acabamento)
else:
    print("NÃO existe uma solução ótima :(")