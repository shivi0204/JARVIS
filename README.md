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

3. JARVIS will prompt you for a password. Enter kartick14 to access full functionality.

4. Speak commands into your microphone prefixed with "JARVIS" (e.g., "JARVIS, open YouTube").

5. Enjoy interacting with JARVIS!

# Commands

**Open Google:** Opens Google in the default web browser.

**Open YouTube:** Opens YouTube in the default web browser.

**Open Instagram:** Opens Instagram in the default web browser.

**What's the time:** Retrieves the current time and speaks it out.

**Play [song name] on YouTube:** Plays the requested song on YouTube.

**Exit:** Shuts down JARVIS.

# Customization
Password: Change the password in the script (pwd='your_password') for security.

Custom Responses: Modify speech responses in the script for personalized interaction.

# Contributing
Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.

# Acknowledgments
1. Inspired by the JARVIS AI from the Marvel Cinematic Universe.

2. Built using Python and various open-source libraries.
