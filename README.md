# EPSILON-DELTA

```bash
The formal definition of a limit (or the epsilon-delta definition)
states that the limit of a function f(x) as x approaches a
is equal to L if, for every tolerance ε > 0, there exists a
corresponding proximity radius δ > 0.
```

```bash
0 < |x – a| < δ, then |f(x) – L| < ε
```

```bash
Enter F(x) (or 0 to exit): 2*x
Enter Eps Limit Tend (separated by spaces): 0.01 2 1
delta = 0.001, i.e. 0.999 < x < 1.001 guarantees |2*x - 2.0| < 0.01
```

```bash
Enter F(x) (or 0 to exit): |x|/x 
Enter Eps Limit Tend (separated by spaces): 0.01 1 0
epsilon = 0.01: no delta tested works for this epsilon.
```
