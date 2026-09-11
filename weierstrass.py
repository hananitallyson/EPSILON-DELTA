import math

def _weierstrass_infinity(f, positive_inf, L, epsilon):
    def is_valid_M(test_M, steps=1000):
        for i in range(steps + 1):
            offset = (i / steps) * 1e6 
            x = test_M + offset if positive_inf else -(test_M + offset)

            try:
                value = f(x)
                if isinstance(value, complex) or math.isnan(value) or math.isinf(value):
                    return False

                if abs(value - L) >= epsilon:
                    return False

            except (ValueError, ZeroDivisionError, OverflowError, TypeError):
                return False

        return True

    low = 0.0
    high = 1.0
    
    while not is_valid_M(high):
        low = high
        high *= 2
        if high > 1e8:  
            return False, None
            
    precision = 1e-4
    while (high - low) > precision:
        mid = (low + high) / 2.0

        if is_valid_M(mid):
            high = mid  
        else:
            low = mid   
            
    return True, round(high, 4)

def weierstrass(f, a, L, epsilon):
    if math.isinf(a):
        return _weierstrass_infinity(f, a > 0, L, epsilon)

    def check_delta(test_delta, steps=1000):
        for i in range(steps, 0, -1):
            d = test_delta * i / steps

            for sign in (-1, 1):
                x = a + sign * d

                try:
                    value = f(x)
                    if isinstance(value, complex) or math.isnan(value) or math.isinf(value):
                        return False, x

                    if abs(value - L) >= epsilon:
                        return False, x

                except (ValueError, ZeroDivisionError, OverflowError, TypeError):
                    return False, x

        return True, None

    low = 0.0
    high = 1.0
    
    valid, cx = check_delta(high)
    
    if valid:
        while True:
            valid, cx = check_delta(high)
            if not valid:
                break
            low = high
            high *= 2
            if high > 1e6:  
                return True, high
    else:
        pass
            
    precision = 1e-7
    while (high - low) > precision:
        mid = (low + high) / 2.0
        valid, _ = check_delta(mid)
        if valid:
            low = mid  
        else:
            high = mid 
            
    if low < 1e-10:
        _, cx = check_delta(0.01)
        return False, cx if cx is not None else (a + 0.001)
        
    return True, round(low, 6)
