import time
from pathlib import Path

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


if __name__ == "__main__":
    print("Testing the action functions...")

    # Test 1: Respond to user
    print("Testing: action_respond_to_user()")
    print("You should hear a whisper sound...")
    action_respond_to_user()
    print("...Test complete.")
