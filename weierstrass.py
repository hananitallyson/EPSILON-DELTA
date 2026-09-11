import math

def weierstrass(f, a, L, epsilon):
    steps = 10000
    low = 0.0
    high = 1.0
    is_valid = True

    while is_valid:
        for i in range(steps, 0, -1):
            d = high * i / steps

            for direction in (-1, 1):
                try:
                    x = a + direction * d

                    if abs(f(x) - L) >= epsilon:
                        is_valid = False
                        break

                except:
                    is_valid = False
                    break

            if not is_valid:
                break

        if is_valid:
            low = high
            high *= 2
            if high > 1e6:
                return True, high

    precision = 1e-7

    while (high - low) > precision:
        mid = (low + high) / 2.0
        valid_mid = True

        for i in range(steps, 0, -1):
            d = mid * i / steps

            for direction in (-1, 1):
                try:
                    x = a + direction * d

                    if abs(f(x) - L) >= epsilon:
                        valid_mid = False
                        break

                except:
                    valid_mid = False
                    break

            if not valid_mid:
                break
        
        if valid_mid:
            low = mid
        else:
            high = mid

    if low < 1e-10:
        for i in range(steps, 0, -1):
            d = 0.01 * i / steps

            for direction in (-1, 1):
                try:
                    x = a + direction * d

                    if abs(f(x) - L) >= epsilon:
                        return False, x

                except:
                    return False, x

        return False, a + 0.001

    return True, round(low, 6)
