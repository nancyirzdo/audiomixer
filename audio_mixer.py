import pyaudio
import wave
import threading
import numpy as np
from tkinter import Tk, Button, Label, filedialog

class AudioSource:
    def __init__(self, filename):
        self.filename = filename
        self._load_audio()

    def _load_audio(self):
        with wave.open(self.filename, 'rb') as wf:
            self.channels = wf.getnchannels()
            self.rate = wf.getframerate()
            self.frames = wf.readframes(wf.getnframes())
            self.np_frames = np.frombuffer(self.frames, dtype=np.int16)

    def get_data(self):
        return self.np_frames

class AudioMixer:
    def __init__(self):
        self.sources = []
        self.output_rate = 44100
        self.output_channels = 2
        self.p = pyaudio.PyAudio()

    def add_source(self, filename):
        source = AudioSource(filename)
        self.sources.append(source)

    def mix_sources(self):
        if not self.sources:
            return None

        mixed_data = np.zeros_like(self.sources[0].get_data())
        for source in self.sources:
            mixed_data = mixed_data + source.get_data()
        
        # Normalize the mixed data to prevent clipping
        mixed_data = mixed_data / len(self.sources)
        return mixed_data.astype(np.int16)

    def play_mixed_audio(self):
        mixed_data = self.mix_sources()
        if mixed_data is None:
            print("No audio sources to mix.")
            return

        stream = self.p.open(format=pyaudio.paInt16,
                             channels=self.output_channels,
                             rate=self.output_rate,
                             output=True)

        stream.write(mixed_data.tobytes())
        stream.stop_stream()
        stream.close()

    def terminate(self):
        self.p.terminate()

class AudioMixerApp:
    def __init__(self):
        self.mixer = AudioMixer()
        self.root = Tk()
        self.root.title("Audio Mixer")

        self.add_button = Button(self.root, text="Add Audio Source", command=self.add_source)
        self.add_button.pack()

        self.play_button = Button(self.root, text="Play Mixed Audio", command=self.mixer.play_mixed_audio)
        self.play_button.pack()

        self.quit_button = Button(self.root, text="Quit", command=self.quit)
        self.quit_button.pack()

    def add_source(self):
        filename = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
        if filename:
            self.mixer.add_source(filename)

    def quit(self):
        self.mixer.terminate()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AudioMixerApp()
    app.run()