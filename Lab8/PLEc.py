import math

def evaluate_functions(x):
    fx = math.cos(2 * x)       
    f1x = -2 * math.sin(2 * x) 
    f2x = -4 * math.cos(2 * x) 
    return fx, f1x, f2x


x = math.pi
fx, f1x, f2x = evaluate_functions(x)

print(f"For x = π:")
print("f(x)  =", fx)
print("f'(x) =", f1x)
print("f''(x) =", f2x)
