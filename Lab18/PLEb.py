import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def load_audio(filename):
    rate, data = wavfile.read(filename)
    if data.ndim > 1:  
        data = data.mean(axis=1)
    data = data / np.max(np.abs(data)) 
    return rate, data

rate1, clean = load_audio("sample.wav")
rate2, noisy = load_audio("sample.wav")
rate3, periodic = load_audio("sample.wav")

if not (rate1 == rate2 == rate3):
    raise ValueError("All audio files must have the same sampling rate!")

def autocorr(x):
    """Compute full autocorrelation (lags -N+1 to N-1)."""
    return np.correlate(x, x, mode='full')

def crosscorr(x, y):
    """Compute full cross-correlation."""
    return np.correlate(x, y, mode='full')

auto_clean = autocorr(clean)
auto_noisy = autocorr(noisy)
auto_periodic = autocorr(periodic)
cross_clean_noisy = crosscorr(clean, noisy)

def normalize_corr(corr):
    return corr / np.max(np.abs(corr))

auto_clean = normalize_corr(auto_clean)
auto_noisy = normalize_corr(auto_noisy)
auto_periodic = normalize_corr(auto_periodic)
cross_clean_noisy = normalize_corr(cross_clean_noisy)

lags_auto = np.arange(-len(clean) + 1, len(clean))
lags_cross = np.arange(-len(clean) + 1, len(noisy))

plt.figure(figsize=(12, 10))

plt.subplot(4, 1, 1)
plt.plot(lags_auto, auto_clean, color='b')
plt.title("Autocorrelation – Clean Audio")
plt.xlabel("Lag")
plt.ylabel("Correlation")

plt.subplot(4, 1, 2)
plt.plot(lags_auto, auto_noisy, color='r')
plt.title("Autocorrelation – Noisy Audio")
plt.xlabel("Lag")
plt.ylabel("Correlation")

plt.subplot(4, 1, 3)
plt.plot(lags_auto, auto_periodic, color='g')
plt.title("Autocorrelation – Periodic Audio")
plt.xlabel("Lag")
plt.ylabel("Correlation")

plt.subplot(4, 1, 4)
plt.plot(lags_cross, cross_clean_noisy, color='m')
plt.title("Cross-Correlation – Clean vs Noisy Audio")
plt.xlabel("Lag")
plt.ylabel("Correlation")

plt.tight_layout()
plt.show()
