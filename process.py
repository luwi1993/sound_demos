from load import WaveLoader
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt
import numpy as np


class Preprocessor:
    def __init__(self):
        pass

    def fft(self, samples):
        return fft(samples)

    def ifft(self, samples):
        return ifft(samples)

    def sine(self, t, f=1, phi=0):
        return np.sin(2 * np.pi * t * f + phi)

    def rect(self, t):
        N = len(t)
        n = int(N/3)
        rect = np.zeros(N)
        rect[n:2*n]=1
        return rect

def test():
    p = Preprocessor()
    w = WaveLoader()
    # samples = w.load()
    # Number of sample points
    N = 600
    # sample spacing
    T = 1.0 / 800.0
    t = np.linspace(0.0, N * T, N)
    samples = p.sine(t,200)

    samples = p.rect(t)
    transform = p.fft(samples)
    restored = p.ifft(transform)
    print(restored - samples)

    xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
    plt.plot(xf, 2.0 / N * np.abs(transform[0:N // 2]))
    plt.grid()
    plt.show()

test()
