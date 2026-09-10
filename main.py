from weierstrass import weierstrass

if __name__ == "__main__":
    # Case 1: Limit exists -> f(x) = 2x, x -> 1, L = 2
    f1 = lambda x: 2 * x
    valid1, delta1, counter1 = weierstrass(f1, a=1.0, L=2.0, epsilon=0.01)
    print(f"\nCase 1 (Success) -> Valid: {valid1} | Delta: {delta1} | Counterexample: {counter1}")

    # Case 2: Limit does not exist -> f(x) = |x| / x, x -> 0, proposed L = 1.0
    f2 = lambda x: abs(x) / x
    valid2, delta2, counter2 = weierstrass(f2, a=0.0, L=1.0, epsilon=0.5)
    print(f"Case 2 (Failure) -> Valid: {valid2} | Delta: {delta2} | Counterexample: {counter2}\n")
