import random
import sys
import numpy as np
from sympy import symbols, sympify, simplify, expand, solve, Matrix

history = []

# Define common symbols for algebra
x, y, z = symbols('x y z')

def chaotic_calculate(expr):
    try:
        # 10% chance for random chaos
        if random.random() < 0.1:
            return f"🤯 Random chaos: {random.randint(-1000,1000)}"

        # Check for algebra commands
        expr_lower = expr.lower()
elif expr_lower.startswith("solve"):
    to_solve = expr[5:].strip()
    # If the input looks like a system with a tuple of symbols
    if to_solve.startswith("[") and "(" in to_solve:
        result = eval(f"solve({to_solve})", {"__builtins__": None}, globals())
    else:
        result = solve(sympify(to_solve))

        elif expr_lower.startswith("simplify"):
            to_simplify = expr[8:].strip()
            result = simplify(sympify(to_simplify))
        elif expr_lower.startswith("expand"):
            to_expand = expr[6:].strip()
            result = expand(sympify(to_expand))
        elif expr_lower.startswith("matrix"):
            # Example: matrix([[1,2],[3,4]])
            matrix_str = expr[6:].strip()
            result = Matrix(eval(matrix_str))
        else:
            # Try symbolic evaluation first
            result = sympify(expr)

        history.append((expr, result))
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Ultimate Calculator (Python CLI)")
    print("Supports: algebra, matrices, vectors, lists, math, chaos")
    print("Commands: solve(...), simplify(...), expand(...), matrix([...])")
    print("Type 'history' to see past calculations, 'exit' to quit.\n")

    while True:
        expr = input("> ").strip()
        if expr.lower() == "exit":
            print("Goodbye! 🌀")
            sys.exit()
        elif expr.lower() == "history":
            if history:
                for i, (e, r) in enumerate(history, 1):
                    print(f"{i}. {e} = {r}")
            else:
                print("No history yet.")
        elif expr:
            print(chaotic_calculate(expr))

if __name__ == "__main__":
    main()
