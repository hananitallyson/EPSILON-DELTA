from weierstrass import weierstrass

if __name__ == "__main__":
    f1 = lambda x: 2 * x
    f1_str = "f(x) = 2*x"
    valid1, delta1, counter1 = weierstrass(f1, a=1.0, L=2.0, epsilon=0.01)
    print(f"\n({f1_str}, a = 1, L = 2, ε = 0.01) -> Valid: {valid1} | Delta: {delta1} | Counterexample: {counter1}")

    f2 = lambda x: abs(x) / x
    f2_str = "f(x) = |x| / x"
    valid2, delta2, counter2 = weierstrass(f2, a=0.0, L=1.0, epsilon=0.5)
    print(f"({f2_str}, a = 0, L = 1, ε = 0.5) -> Valid: {valid2} | Delta: {delta2} | Counterexample: {counter2}\n")
