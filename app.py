import pygame
import flet as ft
import threading
import time

is_metronome_running = False
is_playing_a_tone = False
a_tone_channel = None
metronome_interval = 0.5  # 120 BPM に合わせた値を初期値とする。

pygame.mixer.init()


def create_app(page: ft.Page):
    bpm_label = ft.Text("BPM : 120")
    bpm_range_label = ft.Text("BPM Range : 40 - 240")
    bpm_slider = ft.Slider(value=120, min=40, max=240, divisions=200, label="BPM",
                           on_change=lambda e: update_bpm_from_slider(e, page, bpm_label, bpm_slider))
    start_button = ft.ElevatedButton(text="Start Metronome", on_click=start_metronome)
    stop_button = ft.ElevatedButton(text="Stop Sounds", on_click=stop_sounds)
    tuning_button = ft.ElevatedButton(text="Play 'A' Sound (440 Hz)", on_click=play_a_tone)

    page.add(bpm_label, bpm_range_label, bpm_slider, start_button, stop_button, tuning_button)


def update_bpm_from_slider(e, page, bpm_label, bpm_slider):
    global metronome_interval
    bpm = int(bpm_slider.value)
    bpm_label.value = f"BPM : {bpm}"
    metronome_interval = 60.0 / bpm
    page.update()


def start_metronome(e):
    def _run_metronome():
        click_low = pygame.mixer.Sound("Sound/click_low.wav")
        click_high = pygame.mixer.Sound("Sound/click_high.wav")

        beat = 1
        while is_metronome_running:
            if beat == 1:
                click_high.play()
            else:
                click_low.play()

            time.sleep(metronome_interval)
            beat = (beat % 4) + 1

    global is_metronome_running
    if is_metronome_running:
        return

    stop_sounds(None)

    is_metronome_running = True
    threading.Thread(target=_run_metronome, daemon=True).start()


def stop_sounds(e):
    global is_metronome_running, is_playing_a_tone, a_tone_channel
    is_metronome_running = False

    if is_playing_a_tone and a_tone_channel is not None:
        a_tone_channel.stop()
        is_playing_a_tone = False


def play_a_tone(e):
    global is_playing_a_tone, a_tone_channel

    if is_playing_a_tone:
        return

    stop_sounds(None)

    is_playing_a_tone = True
    a_tone = pygame.mixer.Sound("Sound/A440.wav")
    a_tone_channel = a_tone.play(-1)


ft.app(target=create_app)
