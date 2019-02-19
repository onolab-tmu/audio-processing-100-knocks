# the package 'sounddevice' allow to record and play back
# in a few different ways.
# Documentation is available at https://python-sounddevice.readthedocs.io
import sounddevice as sd

if __name__ == '__main__':

    fs = 44100  # sampling frequency
    duration = 10.  # duration in seconds

    # This function is called upon receiving new data
    def callback(indata, outdata, frames, time, status):
        if status:
            print(status)
        outdata[:] = indata

    # We now start a stream
    with sd.Stream(channels=2, samplerate=fs, callback=callback):
        sd.sleep(int(duration * 1000))
