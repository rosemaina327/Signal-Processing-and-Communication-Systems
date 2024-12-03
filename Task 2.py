import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 1        # Symbol period
f_s = 100    # Sampling frequency (for time domain)
N = 2048     # Number of frequency samples
f = np.linspace(-2, 2, N)  # Frequency range for plotting

# Raised Cosine Filter Frequency Response
def raised_cosine(f, T, r):
    bandwidth = 1 / (2 * T)
    H_f = np.zeros_like(f)
    for i, freq in enumerate(f):
        abs_freq = np.abs(freq)
        if abs_freq <= (1 - r) * bandwidth:
            H_f[i] = 1
        elif abs_freq <= (1 + r) * bandwidth:
            H_f[i] = 0.5 * (1 + np.cos(np.pi * T / r * (abs_freq - bandwidth * (1 - r))))
    return H_f

# Time Domain Response
def time_domain_pulse(t, T, r):
    if r == 0:
        # For r = 0, use the sinc function directly
        return np.sinc(t / T)
    else:
        with np.errstate(divide='ignore', invalid='ignore'):
            sinc_term = np.sinc(t / T)
            cos_term = np.cos(np.pi * r * t / T)
            denom_term = 1 - (2 * r * t / T)**2
            h_t = sinc_term * cos_term / denom_term
            h_t[np.abs(denom_term) < 1e-10] = np.pi / 4 * np.sin(np.pi / (2 * r)) / T
        return h_t

# Plotting
r_values = [0, 0.2, 0.5, 1]
t = np.linspace(-5*T, 5*T, int(f_s * 10 * T))  # Time vector for time domain

plt.figure(figsize=(12, 8))

for r in r_values:
    # Frequency Domain Plot
    H_f = raised_cosine(f, T, r)
    plt.subplot(2, 1, 1)
    plt.plot(f, H_f, label=f"r = {r}")
    
    # Time Domain Plot
    h_t = time_domain_pulse(t, T, r)
    plt.subplot(2, 1, 2)
    plt.plot(t, h_t, label=f"r = {r}")

# Frequency Domain Settings
plt.subplot(2, 1, 1)
plt.title("Raised Cosine Spectrum")
plt.xlabel("Frequency (normalized)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Time Domain Settings
plt.subplot(2, 1, 2)
plt.title("Raised Cosine Pulse in Time Domain")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
