from pulp import *

#Item A  
Z1 = LpProblem("ItemA", LpMaximize)
 
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)

Z1 += 2*x1 + 3*x2 - 5*x3

Z1 += x1 + x2 + x3 == 7
Z1 += 2*x1 - 5*x2 + x3 >= 10

print("Item A)")
if Z1.solve():
    print("Existe uma solução ótima!\n")
    for v in Z1.variables():
        print(v.name, " = ", v.varValue)
    print("Valor máximo: ", value(Z1.objective))
else:
    print("NÃO existe uma solução ótima :(")


#Item B
Z2 = LpProblem("ItemB", LpMinimize)
x4 = LpVariable("x4", lowBound = 0)
x5 = LpVariable("x5", lowBound = 0)
x6 = LpVariable("x6", lowBound = 0)

Z2 += 2*x4 + 3*x5 - 5*x6

Z2 += x4 + x5 + x6 == 7
Z2 += 2*x4 - 5*x5 + x6 >= 10

print("Item B)")
if Z2.solve():
    print("Existe uma solução ótima!\n")
    for v in Z2.variables():
        print(v.name, " = ", v.varValue)
    print("Valor mínimo: ", value(Z2.objective))
else:
    print("NÃO existe uma solução ótima :(")



# Item C
Z3 = LpProblem("ItemC", LpMaximize)
x7 = LpVariable("x7", lowBound = 0)
x8 = LpVariable("x8", lowBound = 0)
x9 = LpVariable("x9", lowBound = 0)

Z3 += x7 + 2*x8 + x9

Z3 += x7 + x8 + x9 == 7
Z3 += 2*x7 - 5*x8 + x9 >= 10

print("Item C)")
if Z3.solve():
    print("Existe uma solução ótima!\n")
    for v in Z3.variables():
        print(v.name, " = ", v.varValue)
    print("Valor máximo: ", value(Z3.objective))
else:
    print("NÃO existe uma solução ótima :(")


# Item D
Z4 = LpProblem("ItemD", LpMinimize)

x10 = LpVariable("x10", lowBound = 0)
x11 = LpVariable("x11", lowBound = 0)
x12 = LpVariable("x12", lowBound = 0)

Z4 += 4*x10 - 8*x11 + 3*x12

Z4 += x10 + x11 + x12 == 7
Z4 += 2*x10 - 5*x11 + x12 >= 10

if Z4.solve():
    print("Existe uma solução ótima!\n")
    for v in Z4.variables():
        print(v.name, " = ", v.varValue)
    print("Valor mínimo da função: ", value(Z4.objective))

else:
    print("NÃO há solução ótima :(")
