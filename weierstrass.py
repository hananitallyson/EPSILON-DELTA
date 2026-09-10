def weierstrass(f, a, L, epsilon=0.01):
    delta = 1.0
    scan_steps = 500

    for _ in range(30): 
        violation_found = False
        counterexample = None

        for i in range(1, scan_steps + 1):
            distance = delta * (i / scan_steps)
            x_left = a - distance
            x_right = a + distance

            for x in (x_left, x_right):
                try:
                    val = f(x)
                    if abs(val - L) >= epsilon:
                        violation_found = True
                        counterexample = x
                        break
                except (ZeroDivisionError, ValueError):
                    violation_found = True
                    counterexample = x
                    break

            if violation_found:
                break

        if not violation_found:
            return True, delta, None

        delta /= 2.0

    return False, None, counterexample
