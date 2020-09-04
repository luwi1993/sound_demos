import wave
import struct
import matplotlib.pyplot as plt

class WaveLoader:
    def __init__(self):
        self.samples = []

    def load(self, path="files/noise.wav"):
        file = wave.open(path, mode="r")
        samples = [struct.unpack("f", file.readframes(2))[0] for i in range(int(file.getnframes() / 2))]
        self.samples = samples
        return samples

    def plot(self, samples=None):
        if type(samples) == None:
            samples = self.samples
        plt.plot(samples)
        plt.show()

def test():
    w = WaveLoader()
    w.load()
    w.plot()