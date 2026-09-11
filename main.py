import math
from weierstrass import weierstrass


def parse_expression(expr):
    replacements = {
        "sqrt": "sqrt",
        "sen": "sin",
        "sin": "sin",
        "cos": "cos",
        "tan": "tan",
        "tg": "tan",
        "asin": "asin",
        "acos": "acos",
        "atan": "atan",
        "ln": "log",
        "log": "log10",
        "abs": "abs",
        "exp": "exp",
        "pi": "pi",
        "e": "e",
    }

    for name, replacement in replacements.items():
        if name in expr:
            expr = expr.replace(name, replacement)

    return expr


if __name__ == "__main__":
    while True:
        data = input("\nEnter F(x) Eps Limit Tend (or 0 to exit): ").split()

        if len(data) == 1 and data[0] == "0":
            print("exit...\n")
            break

        f_str = data[0]
        f_expr = parse_expression(f_str)

        f = eval(
            f"lambda x: {f_expr}",
            {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "asin": math.asin,
                "acos": math.acos,
                "atan": math.atan,
                "log": math.log,
                "log10": math.log10,
                "abs": abs,
                "exp": math.exp,
                "pi": math.pi,
                "e": math.e,
            }
        )

        eps = float(data[1])
        L   = float(data[2])
        a   = float(data[3])

        exists, delta = weierstrass(f, a, L, eps)

        if exists:
            print(f"delta = {delta}, i.e. {a - delta} < x < {a + delta} guarantees |{f_str} - {L}| < {eps}")
        else:
            print(f"epsilon = {eps}: no delta tested works for this epsilon.")
