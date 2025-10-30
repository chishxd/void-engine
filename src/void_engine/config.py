"""Configuration settings and constants for V.O.I.D engine.

This module acts as a single source of truth for all commands and stuff,
the things that are static and will be used throughout the whole codebase...
IDK what things will be here, but for now it's only commands here
"""

# The activate/wake word, liek Hey Google or Hey Siri!
FOCUS_WORD = "void"

# This dictionary all the commands and their descriptions.
# This will be used to display the MANUAL in TUI
COMMANDS = {
    "can you hear me": "Establishes primary link",
    "what are you": "Display the current version",
    "take control": "Enable mouse-free navigation",
    "show me a secret": "Open the application's log",
    "let me out": "Exit",
}
