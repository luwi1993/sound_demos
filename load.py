import wave
import struct
import matplotlib.pyplot as plt

class WaveLoader:
    def __init__(self):
        self.samples = []

    def load(self, path="files/noise.wav"):
        file = wave.open(path, mode="r")
        self.samples = [struct.unpack("f", file.readframes(2)) for i in range(int(file.getnframes() / 2))]

    def plot(self, samples=None):
        if not samples:
            samples = self.samples
        plt.plot(samples)
        plt.show()

w = WaveLoader()
w.load()
w.plot()