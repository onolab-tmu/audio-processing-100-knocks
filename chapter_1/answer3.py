# There exists a number of different libraries to read wav files
# but we can just use the one that comes with Scipy package
from scipy.io import wavfile

# the package 'sounddevice' allow to record and play back
# in a few different ways.
# Documentation is available at https://python-sounddevice.readthedocs.io
import sounddevice as sd

if __name__ == '__main__':

    # choose the file to read and open it
    fn = '../data/cmu_arctic_us_aew_a0001.wav'  # mono
    #fn = '../data/piano2.wav'  # stereo
    fs, audio = wavfile.read(fn)

    # play the file
    sd.play(audio, samplerate=fs, blocking=True)
