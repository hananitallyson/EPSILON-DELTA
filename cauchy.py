import math


def cauchy(f, a, L, epsilon=0.5):
    delta = 1.0
    counterexample = None

    for _ in range(60):
        found = False

        for i in range(1, 1001):
            distance = delta / (i + 1)

            x_left = a - distance
            x_right = a + distance

            if math.fabs(f(x_left) - L) >= epsilon:
                counterexample = x_left
                found = True
                break

            if math.fabs(f(x_right) - L) >= epsilon:
                counterexample = x_right
                found = True
                break

        if not found:
            return None

        delta /= 2

        if delta <= 1e-12:
            break

    return counterexample
