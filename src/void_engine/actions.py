import platform
import subprocess
import time
import tkinter as tk
from pathlib import Path

import pyautogui
import simpleaudio as sa
from PIL import ImageTk


def _play_audio_file(sound_path: Path) -> None:
    system = platform.system()

    if system == "Windows":
        # Windows: Use PowerShell's media player
        subprocess.Popen(
            [
                "powershell",
                "-c",
                f"(New-Object Media.SoundPlayer '{sound_path}').PlaySync()",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    elif system == "Darwin":
        subprocess.Popen(
            ["afplay", str(sound_path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    else:
        subprocess.Popen(
            ["aplay", str(sound_path)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


def action_play_scream() -> None:
    try:
        script_path = Path(__file__).parent.parent.parent
        sound_path = script_path / "sfx" / "scream.wav"
        _play_audio_file(sound_path)

    except Exception as e:
        print(f"Error in action_play_scream: {e}")


def action_play_glitch_sound() -> None:
    try:
        script_path = Path(__file__).parent.parent.parent
        sound_path = script_path / "sfx" / "glitch.wav"
        _play_audio_file(sound_path)

    except Exception as e:
        print(f"Error in action_play_glitch_sound: {e}")


def play_sound(sound_path: Path, duration_seconds: float) -> None:
    wave_obj = sa.WaveObject.from_wave_file(str(sound_path))
    play_obj = wave_obj.play()

    try:
        time.sleep(duration_seconds)
    finally:
        play_obj.stop()


def action_respond_to_user() -> None:
    try:
        script_path = Path(__file__)
        sound_path = script_path.parent.parent.parent / "sfx" / "whispers.wav"
        _play_audio_file(sound_path)

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


def show_image(image_path: str, duration_ms: int):
    root = tk.Tk()

    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.config(cursor="none")

    img = ImageTk.PhotoImage(file=image_path)
    label = tk.Label(root, image=img)
    label.pack()

    root.after(duration_ms, root.destroy)

    root.mainloop()


# def action_glitch_screen() -> None:
#     glitch_file = Path("glitch.png")
#     try:
#         subprocess.run(["scrot", "-o", str(glitch_file)], check=True)

#         # 2. Open the image file we just created with Pillow.
#         with Image.open(glitch_file) as screenshot:
#             # 3. Invert the image.
#             inverted_image = ImageOps.invert(screenshot)
#             # 4. Save the inverted image back to the same file.
#             inverted_image.save(glitch_file)
#         # --- END OF FIX ---

#         for _ in range(3):
#             show_image(str(glitch_file), 100)
#             time.sleep(0.5)

#     except Exception as e:
#         print(f"Error in action_glitch_screen : {e}")
#     finally:
#         if glitch_file.exists():
#             glitch_file.unlink()


if __name__ == "__main__":
    # print("Testing the action functions...")

    # # Test 1: Respond to user
    # print("Testing: action_respond_to_user()")
    # print("You should hear a whisper sound...")
    # action_respond_to_user()
    # print("...Test complete.")
    # action_take_control()
    # action_open_secret_folder()
    pass
