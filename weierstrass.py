import math

def weierstrass(f, a, L, epsilon):
    deltas = [1.0, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 0.00005, 0.00001]

    for delta in deltas:
        valid = True
        steps = 10000

        for i in range(1, steps + 1):
            d = delta * (i / steps)

            for sign in (-1, 1):
                x = a + sign * d

                try:
                    value = f(x)
                    
                    if isinstance(value, complex) or math.isnan(value) or math.isinf(value):
                        valid = False
                        break

                    if abs(value - L) >= epsilon:
                        valid = False
                        break

                except (ValueError, ZeroDivisionError, OverflowError, TypeError):
                    valid = False
                    break

            if not valid:
                break

        if valid:
            return True, delta

    return False, None
