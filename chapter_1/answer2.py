# numpy is used for array/matrix operations
import numpy as np

# the package 'sounddevice' allow to record and play back
# in a few different ways.
# Documentation is available at https://python-sounddevice.readthedocs.io
import sounddevice as sd

if __name__ == '__main__':

    fs = 16000  # sampling frequency
    f_sine = 440.  # frequency of the sine wave
    T = 5.  # length of the sine wave in seconds

    # create the sine wave in a numpy array
    time = np.arange(int(T * fs)) / fs
    wave = np.sin(2. * np.pi * f_sine * time)
    wave *= 0.7  # adjust the volume

    # play back the sine wave
    # the `blocking` keyword stops the execution of the
    # program until the sound finished playing
    sd.play(wave, samplerate=fs, blocking=True)

