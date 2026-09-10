from weierstrass import weierstrass
from cauchy import cauchy


f = lambda x: 2 * x
g = lambda x: 1 if x >= 0 else -1

data = input("inputs (a L): ").split(" ")
target = float(data[0]) 
lim = float(data[1])

print("limit exists:", weierstrass(f, target, lim), "| counterexample:", cauchy(g, target, lim))

