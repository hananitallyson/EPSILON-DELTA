import math
import re
from weierstrass import weierstrass

def parse_expression(expr):
    expr = expr.replace(" ", "")
    expr = re.sub(r'\|([^|]+)\|', r'abs(\1)', expr)
    expr = expr.replace("^", "**")
    expr = re.sub(r'(\d)([a-zA-Z(])', r'\1*\2', expr)
    expr = re.sub(r'(\))([a-zA-Z0-9(])', r'\1*\2', expr)
    
    replacements = {
        r'\bsen\b': 'sin',
        r'\btg\b': 'tan',
        r'\bln\b': 'log',
        r'\blog\b': 'log10',
    }
    
    for pattern, replacement in replacements.items():
        expr = re.sub(pattern, replacement, expr)

    return expr

if __name__ == "__main__":
    safe_dict = {
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

    while True:
        try:
            f_str = input("\nEnter F(x) (or 0 to exit): ").strip()
            
            if f_str == "0":
                print("exit...\n")
                break
                
            data_str = input("Enter Eps Limit Tend (separated by spaces): ").strip()
            data = data_str.split()
            
            if len(data) != 3:
                print("Invalid format. Please enter exactly 3 space-separated values for Eps, Limit, and Tend.")
                continue

            f_expr = parse_expression(f_str)
            f = eval(f"lambda x: {f_expr}", {"__builtins__": {}, **safe_dict})

            eps = float(data[0])
            L   = float(data[1])
            
            a_str = data[2].lower()
            if a_str in ['inf', '+inf']:
                a = float('inf')
            elif a_str == '-inf':
                a = float('-inf')
            else:
                a = float(a_str)

            exists, result_val = weierstrass(f, a, L, eps)

            if exists:
                if math.isinf(a):
                    sign = ">" if a > 0 else "<"
                    m_val = result_val if a > 0 else -result_val
                    print(f"M = \033[32m{result_val}\033[0m, i.e. x {sign} \033[32m{m_val}\033[0m guarantees |\033[32m{f_str} - {L}\033[0m| < \033[32m{eps}\033[0m")
                else:
                    delta = result_val
                    print(f"delta = \033[32m{delta}\033[0m, i.e. \033[32m{a - delta}\033[0m < x < \033[32m{a + delta}\033[0m guarantees |\033[32m{f_str} - {L}\033[0m| < \033[32m{eps}\033[0m")
            else:
                contraexample_x = result_val
                try:
                    fx_val = f(contraexample_x)
                except Exception:
                    fx_val = "undefined"

                print(f"epsilon = \033[32m{eps}\033[0m, counter e.g: x = \033[32m{contraexample_x}\033[0m; \033[32m0\033[0m < |\033[32mx - {a}\033[0m| < delta; |\033[32m{f_str.replace('x', f'{contraexample_x}')} - {L}\033[0m| >= \033[32m{eps}\033[0m")
        
        except Exception as e:
            print(f"Error processing the expression: \033[32m{e}\033[0m")
