import numpy as np
import matplotlib.pyplot as plt


fs = 1000 
f = 10     
T = 1     

t = np.linspace(0, T, T * fs, endpoint=False)

sine_wave = np.sin(2 * np.pi * f * t)

scaled_signal = 3 * sine_wave

plt.figure(figsize=(10, 6))
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.plot(t, scaled_signal, label='Scaled Signal (Factor of 3)')
plt.title('Amplitude Scaling of a Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()