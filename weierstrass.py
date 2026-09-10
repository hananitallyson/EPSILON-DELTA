def weierstrass(f, a, L, epsilon):
    delta = 1.0
    min_delta = 1e-5

    while delta >= min_delta:
        valid = True
        counterexample = None

        for i in range(1, 10001):
            d = delta * (i / 10000)

            for sign in (-1, 1):
                x = a + sign * d

                try:
                    value = f(x)

                    if abs(value - L) >= epsilon:
                        valid = False
                        counterexample = x
                        break

                except (ValueError, ZeroDivisionError, OverflowError):
                    valid = False
                    counterexample = x
                    break

            if not valid:
                break

        if valid:
            return True, round(delta, 5), None

        # Diminui delta
        if delta > 0.1:
            delta -= 0.1
        elif delta > 0.01:
            delta -= 0.01
        elif delta > 0.001:
            delta -= 0.001
        elif delta > 0.0001:
            delta -= 0.0001
        else:
            delta -= 0.00001

        delta = round(delta, 5)

    return False, None, counterexample
