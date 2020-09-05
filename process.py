from load import WaveLoader
from scipy import signal, fft
import matplotlib.pyplot as plt
import numpy as np


class Preprocessor:
    def __init__(self):
        pass

    def spectogram(self, samples, L, N):
        return np.asarray([self.fft(samples[n*L:(n+1)*L]) for n in range(int(N/L))])
#        return signal.spectrogram(np.asarray(samples), fs=fs, window=('tukey',0.25), nperseg=None, noverlap=None, nfft=None,
 #                                detrend='constant', return_onesided=True, scaling='density', axis=-1, mode='psd')

    def fft(self, samples):
        return fft.fft(samples)

    def ifft(self, samples):
        return fft.ifft(samples)

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
    w.load()
    w.print()
    spec = p.spectogram(w.samples, 64 ,w.nframes)
    print(spec.shape)
    plt.imshow(spec.real.T)
    plt.show()
    # Number of sample points
    # N = 600
    # N = w.nframes
    # # sample spacing
    # T = 1.0 / 800.0
    # T = w.framerate
    # t = np.linspace(0.0, N * T, N)
    # samples = p.sine(t,200)
    # samples = p.rect(t)
    # samples = w.samples
    # plt.plot(t, samples)
    # plt.show()
    # transform = p.fft(samples)
    # restored = p.ifft(transform)
    # print(type(restored[0]))
    # print(np.mean(restored.real - samples))
    # print(np.mean(restored.imag))
    # xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
    # plt.plot(xf, 2.0 / N * np.abs(transform[0:N // 2]))
    # plt.grid()
    # plt.show()

test()
