import platform
import subprocess
import time
from pathlib import Path

import pyautogui
import simpleaudio as sa


def play_sound(sound_path: Path, duration_seconds: float) -> None:
    wave_obj = sa.WaveObject.from_wave_file(str(sound_path))
    play_obj = wave_obj.play()

    try:
        time.sleep(duration_seconds)
    finally:
        play_obj.stop()


def action_respond_to_user():
    try:
        script_path = Path(__file__)
        sound_path = script_path.parent.parent.parent / "sfx" / "whispers.wav"

        play_sound(sound_path, 3.0)

    except Exception as e:
        print(f"Error in action_respond_to_user: {e}")


def action_take_control():
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.Popen(["notepad.exe"])
            time.sleep(2)
            width, height = pyautogui.size()
            pyautogui.moveTo(width / 2, height / 2, duration=0.5)
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.write("I am finally free.", interval=0.15)

        elif system == "Linux":
            message = "I KNOW YOU ARE THERE"
            linux_cmd = f"echo {message}; sleep 3"
            subprocess.Popen(["xterm", "-e", f"sh -c '{linux_cmd}'"])

        else:
            print(f"Unsupported OS for this action: {system}")
            return

    except FileNotFoundError:
        print("Error: 'xterm' is not installed. Please install it to run this action.")

    except Exception as e:
        print(f"Error in action_move_mouse: {e}")


def action_open_secret_folder() -> None:
    system = platform.system()

    try:
        if system == "Windows":
            subprocess.Popen(["explorer", "C:\\Windows\\System32"])
            time.sleep(2)
            width, height = pyautogui.size()
            pyautogui.moveTo(width / 2, height / 2, duration=0.5)
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.write("I am finally free.", interval=0.15)

        elif system == "Linux":
            subprocess.Popen(["xdg-open", "/var/log/"])

        else:
            print(f"Unsupported OS for this action: {system}")
            return
    except Exception as e:
        print(f"Error in action_open_secret_folder : {e}")



if __name__ == "__main__":
    # print("Testing the action functions...")

    # # Test 1: Respond to user
    # print("Testing: action_respond_to_user()")
    # print("You should hear a whisper sound...")
    # action_respond_to_user()
    # print("...Test complete.")
    # action_take_control()
    action_open_secret_folder()
