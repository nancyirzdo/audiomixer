# AudioMixer

AudioMixer is a simple Python program that provides an interface to manage and mix multiple audio sources on Windows. It allows users to add multiple WAV audio files and play them mixed together.

## Features

- Add multiple WAV audio sources
- Mix audio sources together
- Play the mixed audio
- Simple GUI using Tkinter

## Requirements

- Python 3.x
- `pyaudio` library
- `numpy` library
- `Tkinter` (usually included with Python)

## Installation

1. Clone this repository or download the `audio_mixer.py` file.
2. Install the required Python packages using pip:
   ```bash
   pip install pyaudio numpy
   ```

## Usage

1. Run the `audio_mixer.py` script:
   ```bash
   python audio_mixer.py
   ```

2. Use the "Add Audio Source" button to select WAV files you want to mix.
3. Click "Play Mixed Audio" to hear the mixed result.
4. Use the "Quit" button to close the application.

## Notes

- Currently, the program only supports WAV files due to the simplicity of handling this format.
- The mixed audio is normalized to prevent clipping.

## License

This project is licensed under the MIT License - see the LICENSE file for details.