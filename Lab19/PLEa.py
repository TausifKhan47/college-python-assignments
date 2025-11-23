import sympy as sp

def z_transform_unit_step():
    # Define symbols
    n, z = sp.symbols('n z')

    # Unit step function u[n] = 1 for n >= 0
    u = sp.Heaviside(n)

    # Compute Z-transform
    U_z = sp.summation(u * z**(-n), (n, 0, sp.oo))

    print("Z-transform of unit step u[n]:")
    print("U(z) =", U_z)

    # Simplify the expression
    U_z_simplified = sp.simplify(U_z)
    print("\nSimplified:")
    print("U(z) =", U_z_simplified)

    # ROC (Region of Convergence)
    print("\nRegion of Convergence (ROC): |z| > 1")

    # Stability check:
    # A system is stable if ROC includes the unit circle |z| = 1
    if 1 > 1:  # ROC: |z| > 1 NEVER includes |z| = 1
        print("System: Stable")
    else:
        print("System: Unstable")


# Run the function
z_transform_unit_step()
