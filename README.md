# JARVIS: Python Virtual Assistant

JARVIS is a Python-based virtual assistant inspired by Tony Stark's AI assistant in the Marvel Cinematic Universe. This project utilizes various libraries and APIs to enable voice-controlled interaction with the computer.

## Features

- **Voice Recognition**: Utilizes SpeechRecognition library to recognize voice commands.
- **Web Interaction**: Can open websites like Google, YouTube, and Instagram using webbrowser module.
- **Time Display**: Provides current time upon command using datetime library.
- **YouTube Music Playback**: Plays requested music on YouTube via PyWhatKit library.
- **Voice Output**: Uses pyttsx3 library for speech synthesis to respond to user commands.
- **Customizable Responses**: Differentiates responses based on time of day and user authorization.

## Requirements

Ensure you have Python 3.x installed along with the following libraries:
- `speech_recognition`
- `pyttsx3`
- `numpy`
- `pywhatkit`

Install these dependencies using pip:

```bash
pip install speech_recognition pyttsx3 numpy pywhatkit
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your_username/jarvis-python.git
cd jarvis-python
```

2. Run the jarvis.py script:

```bash
python jarvis.py
```
