import math


def weierstrass(f, a, L, epsilon=0.001):
    delta = 1.0

    for _ in range(100):
        valid = True

        for i in range(1, 1001):
            x = a + delta * i / 1000

            if math.fabs(f(x) - L) >= epsilon:
                valid = False
                break

        if valid:
            return True, delta

        delta /= 2

    return False, None


def cauchy(f, a, L, epsilon=0.5):
    delta = 1.0

    for _ in range(100):
        valid = True

        for i in range(1, 1001):
            x = a + delta * i / 1000

            if math.fabs(f(x) - L) >= epsilon:
                valid = False
                break

        if valid:
            return None

        delta /= 2

    return a

f = lambda x: 2 * x
g = lambda x: 1 if x >= 0 else -1

data = input("inputs (a L): ").split(" ")
target = float(data[0]) 
lim = float(data[1])

print("limit exists:", weierstrass(f, target, lim), "| counterexample:", cauchy(g, target, lim))

