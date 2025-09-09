import numpy as np
import matplotlib.pyplot as plt

fs = 500 
T = 2    
t = np.linspace(0, T, T * fs, endpoint=False)  

f1 = 5
sine_wave = np.sin(2 * np.pi * f1 * t)

f2 = 10
cosine_wave = np.cos(2 * np.pi * f2 * t)

multiplied_signal = sine_wave * cosine_wave

plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plt.plot(t, sine_wave)
plt.title('5 Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, cosine_wave)
plt.title('10 Hz Cosine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, multiplied_signal)
plt.title('Result of Sine Wave Multiplied by Cosine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()