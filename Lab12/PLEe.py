import numpy as np
import matplotlib.pyplot as plt

fs = 1000 
f = 5   
T = 1      


t = np.linspace(0, T, T * fs, endpoint=False)

sine_wave = np.sin(2 * np.pi * f * t)

reversed_signal = np.flip(sine_wave)

plt.figure(figsize=(10, 6))
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.plot(t, reversed_signal, label='Time-Reversed Sine Wave', linestyle='--')
plt.title('Time Reversal of a Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()