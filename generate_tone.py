import numpy as np
from scipy.io.wavfile import write


def generate_tone(frequency, duration, sample_rate=44100, volume=0.5):
    num_samples = int(sample_rate * duration)

    t = np.linspace(0, duration, num_samples, False)
    tone = np.sin(frequency * t * 2 * np.pi)

    audio = tone * (2 ** 15 - 1) * volume
    audio = audio.astype(np.int16)
    return audio

# Aの音
a_frequency = 440
a_duration = 2
a_sound = generate_tone(a_frequency, a_duration)
write("Sound/A440.wav", 44100, a_sound)

# メトロノームの低い音
low_click_frequency = 880
low_click_duration = 0.1
low_click_sound = generate_tone(low_click_frequency, low_click_duration)
write("Sound/click_low.wav", 44100, low_click_sound)

# メトロノームの高い音
high_click_frequency = 1760
high_click_duration = 0.1
high_click_sound = generate_tone(high_click_frequency, high_click_duration)
write("Sound/click_high.wav", 44100, high_click_sound)
