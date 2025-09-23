import sympy as sp

n, z = sp.symbols('n z')

x_n = 3*n

X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

X_z_simplified = sp.simplify(X_z)

print("Z-transform of x[n] = 3n u[n]:")
sp.pprint(X_z_simplified, use_unicode=True)
