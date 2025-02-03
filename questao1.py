from pulp import *

# Definição do problema 
Z = LpProblem("MaximoDeLucro", LpMaximize)

#Criando as variaveis do problema
# carteira = x1 / estojo = x2 / mochila = x3 
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)

#Função Objetivo
Z += 24*x1 + 22*x2 + 45*x3

#Definir as Restrições 

