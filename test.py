import math

def g(x):
    return math.sqrt(x)

def avg_rate(a, b):
    return (g(b) - g(a)) / (b - a)

# Part (a): average rate over [1, 2] and [1, 1.5]
print("Part (a)")
print(f"[1, 2]   : {avg_rate(1, 2):.4f}")
print(f"[1, 1.5] : {avg_rate(1, 1.5):.4f}")

# Part (b): table of average rate over [1, 1+h] as h -> 0
print("\nPart (b)")
print(f"{'h':>10} | {'average rate':>14}")
for h in [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]:
    print(f"{h:>10} | {avg_rate(1, 1 + h):>14.7f}")

# Part (d): exact limit using sympy (install with: pip install sympy)
import sympy as sp
h = sp.symbols("h", positive=True)
expr = (sp.sqrt(1 + h) - 1) / h
print("\nPart (d)")
print("limit as h -> 0:", sp.limit(expr, h, 0))