import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift, fftfreq

# Parameters
T = 1.0  # Width of the triangular pulse
fs = 1000  # Sampling frequency
t = np.arange(-2*T, 2*T, 1/fs)  # Time vector

# Define triangular pulse
pulse = np.where(np.abs(t) <= T, 1 - np.abs(t)/T, 0)  # Creates a triangular pulse centered at t=0

# Compute Fourier transform
freqs = fftshift(fftfreq(len(t), d=1/fs))
spectrum = fftshift(np.abs(fft(pulse)))

# Ploting the triangular pulse
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(t, pulse)
plt.title("Triangular Pulse (Time Domain)")
plt.xlabel("Time")
plt.ylabel("Amplitude")

# Ploting the spectrum
plt.subplot(1, 2, 2)
plt.plot(freqs, spectrum)
plt.title("Spectrum of Triangular Pulse (Frequency Domain)")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.tight_layout()
plt.show()
