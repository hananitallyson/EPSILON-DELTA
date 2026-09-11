import os
import math
import re
from weierstrass import weierstrass

def clean_expression(expression):
    expression = expression.replace(" ", "")
    expression = re.sub(r'\|([^|]+)\|', r'abs(\1)', expression)
    expression = expression.replace("^", "**")
    expression = re.sub(r'(\d)([a-zA-Z(])', r'\1*\2', expression)
    expression = re.sub(r'(\))([a-zA-Z0-9(])', r'\1*\2', expression)
    
    replacements = {
        r'\bsen\b': 'sin',
        r'\btg\b': 'tan',
        r'\bln\b': 'log',
        r'\blog\b': 'log10',
    }
    
    for pattern, replacement in replacements.items():
        expression = re.sub(pattern, replacement, expression)

    return expression

if __name__ == "__main__":
    math_functions = {
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

    os.system("cls" if os.name == "nt" else "clear")

    while True:
        try:
            func_text = input("\nEnter F(x) (0 to exit, - to clear): ").strip()
            
            if func_text == "0":
                print("Exiting...\n")
                break
            if func_text == "-":
                os.system("cls" if os.name == "nt" else "clear")
                continue
                
            data_text = input("Enter Eps, Limit, and Tendency (space-separated): ").strip()
            data_list = data_text.split()
            
            if len(data_list) != 3:
                print("Invalid format. Please enter exactly 3 space-separated values.")
                continue

            ready_expression = clean_expression(func_text)
            func = eval(f"lambda x: {ready_expression}", {"__builtins__": {}, **math_functions})

            epsilon = float(data_list[0])
            limit_val = float(data_list[1])
            point_a = float(data_list[2])

            delta_exists, result = weierstrass(func, point_a, limit_val, epsilon)

            if delta_exists:
                delta = result
                print(f"delta = \033[32m{delta}\033[0m, i.e., \033[32m{point_a - delta}\033[0m < x < \033[32m{point_a + delta}\033[0m guarantees |\033[32m{func_text} - {limit_val}\033[0m| < \033[32m{epsilon}\033[0m")
            else:
                counter_example_x = result
                print(f"epsilon = \033[32m{epsilon}\033[0m, counter e.g: x = \033[32m{counter_example_x}\033[0m; \033[32m0\033[0m < |\033[32mx - {point_a}\033[0m| < delta; |\033[32m{func_text.replace('x', f'{counter_example_x}')} - {limit_val}\033[0m| >= \033[32m{epsilon}\033[0m")
        
        except Exception as error:
            print(f"Error processing expression: \033[32m{error}\033[0m")
