import wave
import struct
import matplotlib.pyplot as plt

class WaveLoader:
    def __init__(self):
        self.samples = []
        self.file = None
        self.nframes = 0
        self.nchannels = 0
        self.framerate = 0
        self.fs = 1
        self.compression = None

    def load(self, path="files/noise.wav"):
        self.file = wave.open(path, mode="r")
        self.nframes = self.file.getnframes()/2
        self.nchannels = self.file.getnchannels()
        self.framerate = self.file.getframerate()
        self.compression = self.file.getcomptype()
        self.fs = 1/self.framerate
        self.samples = [struct.unpack("f", self.file.readframes(2))[0] for i in range(int(self.file.getnframes() / 2))]
        return self.samples

    def print(self):
        print("file",self.file)
        print("nframes", self.nframes)
        print("nchannels", self.nchannels)
        print("framerate", self.framerate)
        print("compression", self.compression)
        print("samples", self.samples[:4])

    def plot(self, samples=None):

        if type(samples) == None:
            samples = self.samples
        plt.plot(samples)
        plt.show()

def test():
    w = WaveLoader()
    w.load()
    w.print()

