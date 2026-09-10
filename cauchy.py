import math


def cauchy(f, a, L, epsilon=0.5):
    delta = 1.0
    counterexample = None

    for _ in range(100):
        found = False

        for i in range(1, 1001):
            distance = delta * i / 1000

            x_left = a - distance
            x_right = a + distance

            if (x_left != a and math.fabs(f(x_left) - L) >= epsilon):
                counterexample = x_left
                found = True
                break

            if (x_right != a and math.fabs(f(x_right) - L) >= epsilon):
                counterexample = x_right
                found = True
                break

        if not found:
            return None

        delta /= 2

    return counterexample
