# There exists a number of different libraries to read wav files
# but we can just use the one that comes with Scipy package
from scipy.io import wavfile

# the package 'sounddevice' allow to record and play back
# in a few different ways.
# Documentation is available at https://python-sounddevice.readthedocs.io
import sounddevice as sd

if __name__ == '__main__':

    # choose the sampling frequency to use
    fs = 44100

    # and the recording time
    T = 5.

    # record, here too blocking mode stops execution until recording is over
    audio = sd.rec(int(fs * T), samplerate=fs, blocking=True, channels=1)

    # re-play the recorded signal
    sd.play(audio, samplerate=fs, blocking=True)
