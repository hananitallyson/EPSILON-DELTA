import math
from cauchy import cauchy
from weierstrass import weierstrass

expr_str = input("\nEnter the expression for f(x) (use 'x' as the variable): ")

f = lambda x: eval(expr_str, {"x": x, "math": math})

data = input("inputs (a L): ").split(" ")
target = float(data[0]) 
lim = float(data[1])

valid, delta = weierstrass(f, target, lim)
counterexample = cauchy(f, target, lim)

print(f"valid: {valid} | delta: {delta} | counterexample: {counterexample}\n")
