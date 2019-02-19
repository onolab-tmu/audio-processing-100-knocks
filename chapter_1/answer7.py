# numpy is used for array/matrix operations
import numpy as np

# There exists a number of different libraries to read wav files
# but we can just use the one that comes with Scipy package
from scipy.io import wavfile

if __name__ == '__main__':

    fs = 16000  # sampling frequency
    f_sine = 440.  # frequency of the sine wave
    delta_f = 5.  # frequency offset of second channel
    T = 5.  # length of the sine wave in seconds

    # create the sine wave in a numpy array
    time = np.arange(int(T * fs)) / fs

    # create the empty array of the correct shape
    n_samples = time.shape[0]
    wave = np.zeros((n_samples, 2))

    wave[:,0] = np.sin(2. * np.pi * f_sine * time)  # channel 1
    wave[:,1] = np.sin(2. * np.pi * (f_sine + delta_f) * time)  # channel 2
    wave *= 0.7  # adjust the volume

    # In 16 bit wave files, the values go from `-2 ** 15` to `2 ** 15 - 1`
    wave_int16 = (wave * (2 ** 15 - 1)).astype(np.int16)

    # now save using scipy, the function infers the file
    # type from the data type of the numpy array
    wavfile.write('samples/question7.wav', fs, wave_int16)
