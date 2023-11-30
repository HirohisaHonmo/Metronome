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
A_FREQUENCY = 440
A_DURATION = 2
a_sound = generate_tone(A_FREQUENCY, A_DURATION)
write("Sound/A440.wav", 44100, a_sound)

# メトロノームの低い音
LOW_CLICK_FREQUENCY = 880
LOW_CLICK_DURATION = 0.1
low_click_sound = generate_tone(LOW_CLICK_FREQUENCY, LOW_CLICK_DURATION)
write("Sound/click_low.wav", 44100, low_click_sound)

# メトロノームの高い音
HIGH_CLICK_FREQUENCY = 1760
HIGH_CLICK_DURATION = 0.1
high_click_sound = generate_tone(HIGH_CLICK_FREQUENCY, HIGH_CLICK_DURATION)
write("Sound/click_high.wav", 44100, high_click_sound)
