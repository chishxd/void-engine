# V.O.I.D Engine
Welcome to the V.O.I.D Engine! A delightful way to communicate with your computer! Please report any unusual behaviours...

## A New Companion
Tired of typing?? We were too. And that's why we present to you, **V**irtualised **O**bject **I**njection **D**aemon, a state-of-art interface that listens to your voice commands to perform several system actions.

## Documented Commands
This engine comes equipped with many voice commands, once awakened, simply use the focus word "void" later followed by our command!

- Establish a link with engine
- Request Visual Feedback from the system
- Interact with your desktop environment
- and much more...

## Getting Started
Ready to meet your new companion? Here’s how to get it running.

Prerequisites:

- Python 3.12+

- uv (https://github.com/astral-sh/uv)

- You may need to install PortAudio for the microphone to work (sudo apt-get install portaudio19-dev on Debian/Ubuntu, sudo dnf install portaudio-devel on Fedora).

## Installation and Usage

Simply run:
```shell
uv run void-engine
```

It will install and run the engine for you

But if you wanna install it in a harder way, or if `uv run` does not work:

Clone the repo
```shell
git clone https://github.com/chishxd/void-engine.git && cd void-engine
```
Create a venv and install dependencies
```shell
uv venv
uv sync
```
Run the project
```shell
uv run void-engine
```

## Usage
1. Once the TUI loads, type `awaken` and press `Enter`
2. The engine is now listening... Speak your commands in the mic clearly
3. Remember to say 'void' before the command, e.g "void, Can you hear me?"

Built with:
- Python
- Textual
- SpeechRecognition

and... <img src="https://upload.wikimedia.org/wikipedia/commons/8/8e/Undertale_red_soul.svg" height="20" style="vertical-align: text-top;"> DETERMINATION
