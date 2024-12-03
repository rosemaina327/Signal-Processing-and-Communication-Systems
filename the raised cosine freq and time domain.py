import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fftshift, fft, ifft

# Define parameters
alpha = 0.5  # Roll-off factor
B = 1  # Bandwidth
T = 1 / B  # Symbol period
f = np.linspace(-3, 3, 1000)  # Frequency range for plotting

# Frequency domain response of the raised cosine filter
def raised_cosine(f, B, alpha):
    H = np.zeros_like(f)
    for i, freq in enumerate(f):
        abs_freq = abs(freq)
        if abs_freq <= B * (1 - alpha) / 2:
            H[i] = 1
        elif B * (1 - alpha) / 2 < abs_freq <= B * (1 + alpha) / 2:
            H[i] = 0.5 * (1 + np.cos(np.pi * (abs_freq - B * (1 - alpha) / 2) / (alpha * B)))
    return H

H_f = raised_cosine(f, B, alpha)

# Time domain response via Inverse FFT (iFFT)
time_pulse = np.fft.ifftshift(ifft(fftshift(H_f)))
t = np.linspace(-5, 5, len(time_pulse))

# Plot Frequency and Time Domain
plt.figure(figsize=(12, 6))

# Frequency Domain (Raised Cosine Filter)
plt.subplot(1, 2, 1)
plt.plot(f, H_f)
plt.title("Raised Cosine Filter (Frequency Domain)")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid(True)

# Time Domain (Raised Cosine Pulse)
plt.subplot(1, 2, 2)
plt.plot(t, np.real(time_pulse))
plt.title("Raised Cosine Pulse (Time Domain)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
