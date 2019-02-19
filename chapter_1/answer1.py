# numpy is used for array/matrix operations
import numpy as np

# There exists a number of different libraries to read wav files
# but we can just use the one that comes with Scipy package
from scipy.io import wavfile

# This package is used to create figures and plots
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # this is a mono file
    fn = '../data/cmu_arctic_us_aew_a0001.wav'  # mono sample
    #fn = '../data/piano2.wav'  # stereo sample
    fs, audio = wavfile.read(fn)

    # here we determine the number of channels
    # if the file is mono, the array `audio` is 1D with shape `(n_samples,)` (the number of samples)
    # if the file has more than one channel, the array is 2D with shape `(n_samples, n_channels,)`
    if audio.ndim == 1:
        n_channels = 1  # file is mono
    else:
        n_channels = audio.shape[1]  # file is multichannel

    # we determine the format of the file
    if audio.dtype == np.float:
        fmt = 'float32'
    elif audio.dtype == np.int32:
        fmt = 'int32'
    elif audio.dtype == np.int16:
        fmt = 'int16'
    else:
        fmt = 'other'  # catch all for unusual formats

    # this will print a message in the terminal
    print('The sampling frequency is:', fs, 'format:', fmt, 'channels:', n_channels)

    # create the x axis time vector
    time = np.arange(audio.shape[0]) / fs

    # this will create the plot
    plt.plot(time, audio)

    # this adds a legend to the x axis
    plt.xlabel('Time [s]')

    # this creates a title for the plot
    # note how we can add latex-like commands
    plt.title('An audio sample with $f_s={}$ Hz'.format(fs))

    # this saves the plot as a PNG figure
    # to save a pdf, replace 'png' by 'pdf', other formats are also available
    plt.savefig('figures/question1.png')

    # this will display the plot on screen
    plt.show()


