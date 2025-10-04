import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import convolve

audio_rate, audio = wavfile.read("sample.wav")
ir_rate, ir = wavfile.read("sample.wav")

if audio_rate != ir_rate:
    raise ValueError("Sampling rates of audio and impulse response must match")

if audio.ndim > 1:
    audio = audio.mean(axis=1)
if ir.ndim > 1:
    ir = ir.mean(axis=1)

audio = audio / np.max(np.abs(audio))
ir = ir / np.max(np.abs(ir))

linear_conv = convolve(audio, ir, mode='full')

N = max(len(audio), len(ir))
X = np.fft.fft(audio, N)
H = np.fft.fft(ir, N)
circular_conv = np.fft.ifft(X * H).real

N_pad = len(audio) + len(ir) - 1
X_pad = np.fft.fft(audio, N_pad)
H_pad = np.fft.fft(ir, N_pad)
circular_conv_padded = np.fft.ifft(X_pad * H_pad).real

linear_conv /= np.max(np.abs(linear_conv))
circular_conv /= np.max(np.abs(circular_conv))
circular_conv_padded /= np.max(np.abs(circular_conv_padded))

plt.figure(figsize=(12, 8))

plt.subplot(3,1,1)
plt.plot(linear_conv, color='b')
plt.title("Linear Convolution Result (True System Output)")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.subplot(3,1,2)
plt.plot(circular_conv, color='r')
plt.title("Circular Convolution (Without Padding) – Time Aliasing Present")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.subplot(3,1,3)
plt.plot(circular_conv_padded, color='g')
plt.title("Circular Convolution (Zero-Padded, Matches Linear)")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

from scipy.io.wavfile import write
write("linear_conv_output.wav", audio_rate, (linear_conv * 32767).astype(np.int16))
write("circular_conv_output.wav", audio_rate, (circular_conv * 32767).astype(np.int16))
