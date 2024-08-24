import soundcard as sc
import numpy as np
import matplotlib.pyplot as plt
SAMPLE_RATE = 44100
TIME_WINDOW = 0.02   # seconds


def split_audio_into_frequency_bands(data: np.array) -> np.array:
    """
        get the audio levels for different frequency bands
    """
    multiplier = 1
    max_freq = 1000
    min_freq = 80
    num_bands = 10
    step = max_freq / num_bands
    # data is of shape (n, 2) where n is the number of samples and 2 is the number of channels
    # we will take the mean of the two channels
    data = np.mean(data, axis=1)
    data = np.abs(data) * multiplier
    # get the fft of the data
    fft = np.fft.rfft(data)
    # get the frequencies
    freqs = np.fft.rfftfreq(len(data), d=1/SAMPLE_RATE)
    # get the power of the fft
    power = np.abs(fft)
    # get the power in different frequency bands
    split_audio_levels = []
    for i in range(min_freq, max_freq, int(step)):
        split_audio_levels.append(
            np.mean(power[(freqs >= i) & (freqs < i + step)]))
    return np.array(split_audio_levels)


def get_audio_levels():

    # get a list of all microphones:v
    mics = sc.all_microphones(include_loopback=True)
    # get the current default microphone on your system:
    default_mic = mics[0]

    with default_mic.recorder(samplerate=SAMPLE_RATE) as mic:
        data = mic.record(numframes=SAMPLE_RATE * TIME_WINDOW)
        split_audio_levels = split_audio_into_frequency_bands(data)
        return split_audio_levels
