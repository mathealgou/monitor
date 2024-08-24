import soundcard as sc
import numpy as np
SAMPLE_RATE = 44100
TIME_WINDOW = 0.01   # seconds


def split_audio_into_frequency_bands(data):
    """
        get the audio levels for different frequency bands
    """
    # split the audio data into 8 frequency bands
    # 0-100Hz, 100-200Hz, 200-400Hz, 400-800Hz, 800-1600Hz, 1600-3200Hz, 3200-6400Hz, 6400-12800
    # the last band will contain the rest of the audio data
    frequency_bands = np.array_split(data, 8)
    # calculate the audio levels for each frequency band
    audio_levels = [np.mean(np.abs(f)) for f in frequency_bands]

    # normalize the audio levels
    audio_levels = np.array(audio_levels) / np.max(audio_levels)
    return audio_levels


def get_audio_levels():
    # get a list of all speakers:
    speakers = sc.all_speakers()
    # get the current default speaker on your system:
    default_speaker = speakers[0]

    # get a list of all microphones:v
    mics = sc.all_microphones(include_loopback=True)
    # get the current default microphone on your system:
    default_mic = mics[0]

    with default_mic.recorder(samplerate=SAMPLE_RATE) as mic, \
            default_speaker.player(samplerate=SAMPLE_RATE) as sp:
        data = mic.record(numframes=SAMPLE_RATE * TIME_WINDOW)
        split_audio_levels = split_audio_into_frequency_bands(data)
        return split_audio_levels
