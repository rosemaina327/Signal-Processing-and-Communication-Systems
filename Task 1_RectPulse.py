"""
Question 1
Use Fourier transforms to analytically show that a rectangular pulse has infinite bandwidth. Use MATLAB or Python to draw the triangular pulse in time domain and its spectrum. Correctly label and mark your axes.
"""



import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift, fftfreq

# Parameters
T = 1.0  # Width of the rectangular pulse
fs = 1000  # Sampling frequency
t = np.arange(-2*T, 2*T, 1/fs)  # Time vector

# Define rectangular pulse
pulse = np.where(np.abs(t) <= T/2, 1, 0)  # Ensure pulse has the same shape as t

# Compute Fourier transform
freqs = fftshift(fftfreq(len(t), d=1/fs))
spectrum = fftshift(np.abs(fft(pulse)))

# Plot the rectangular pulse
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)  # First subplot
plt.plot(t, pulse)
plt.title("Rectangular Pulse (Time Domain)")
plt.xlabel("Time")
plt.ylabel("Amplitude")

# Plot the spectrum
plt.subplot(1, 2, 2)  # Second subplot
plt.plot(freqs, spectrum)
plt.title("Spectrum of Rectangular Pulse (Frequency Domain)")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.tight_layout()
plt.show()
