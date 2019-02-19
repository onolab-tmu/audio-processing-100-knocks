# numpy is used for array/matrix operations
import numpy as np

# the samplerate package can be used to change the sampling frequency of signals
import samplerate

# There exists a number of different libraries to read wav files
# but we can just use the one that comes with Scipy package
from scipy.io import wavfile


if __name__ == '__main__':

    fs_target = 8000

    # this is a mono file
    fn = '../data/cmu_arctic_us_aew_a0001.wav'  # mono sample
    #fn = '../data/piano2.wav'  # stereo sample
    fs, audio = wavfile.read(fn)

    # now do the rate conversion
    # the parameter to provide is the ratio of new to old sampling frequencies
    audio_8k = samplerate.resample(audio, fs_target / fs)

    # the resampling operation returns a float array
    # so we need to recast it to the same original
    # type of the audio file to make sure the range matches
    audio_8k = audio_8k.astype(audio.dtype)

    # now save to a file
    wavfile.write('samples/question8.wav', fs_target, audio_8k)
