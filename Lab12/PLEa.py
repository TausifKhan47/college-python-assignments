import numpy as np
import matplotlib.pyplot as plt


fs = 1000  
t = np.linspace(0, 1, fs, endpoint=False) 


f1 = 5
sine_wave1 = np.sin(2 * np.pi * f1 * t)


f2 = 10
sine_wave2 = np.sin(2 * np.pi * f2 * t)


combined_signal = sine_wave1 + sine_wave2


plt.figure(figsize=(12, 8))


plt.subplot(3, 1, 1)
plt.plot(t, sine_wave1)
plt.title('5 Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, sine_wave2)
plt.title('10 Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, combined_signal)
plt.title('Combined Signal (5 Hz + 10 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()