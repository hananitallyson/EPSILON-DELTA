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
