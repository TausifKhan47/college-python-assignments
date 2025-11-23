import numpy as np
from scipy.signal import dlti
import matplotlib.pyplot as plt

def analyze_system(num, den):
    # Create discrete-time LTI system
    system = dlti(num, den)

    # Extract zeros and poles
    zeros = system.zeros
    poles = system.poles

    print("Zeros:", zeros)
    print("Poles:", poles)

    # Stability: all poles must be inside the unit circle
    stable = all(np.abs(p) < 1 for p in poles)

    if stable:
        print("\nSystem is: STABLE")
    else:
        print("\nSystem is: UNSTABLE")

    # Plot pole-zero diagram
    plt.figure(figsize=(6,6))
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
    plt.gca().add_patch(unit_circle)

    # Plot poles and zeros
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', label='Zeros')
    plt.scatter(np.real(poles), np.imag(poles), marker='x', label='Poles', color='red')

    plt.title("Pole-Zero Plot")
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()


# System: H(z) = 0.5 z^-1 - 0.7 z^-2 - 0.9 z^-3 - 0.6 z^-4 - 0.4 z^-5
num = [0, 0.5, -0.7, -0.9, -0.6, -0.4]  # numerator coefficients
den = [1]                               # denominator for FIR system

analyze_system(num, den)
