import numpy as np
import matplotlib.pyplot as plt


fs = 100  
f = 5    
T = 1     
shift = 0.1 

t = np.linspace(0, T, T * fs, endpoint=False) 
t_shifted = t + shift 

sine_wave = np.sin(2 * np.pi * f * t)
shifted_sine_wave = np.sin(2 * np.pi * f * (t - shift))


plt.figure(figsize=(10, 6))
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.plot(t_shifted, sine_wave, label=f'Shifted by {shift}s (using t + shift)')
plt.plot(t, shifted_sine_wave, '--', label=f'Shifted by {shift}s (using t - shift)')
plt.title('Time Shift of a Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()