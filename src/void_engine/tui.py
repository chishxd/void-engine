import asyncio
import random
import subprocess

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header, Input, Static

from void_engine.actions import (
    action_open_secret_folder,
    action_play_glitch_sound,
    action_play_scream,
    action_respond_to_user,
    action_take_control,
)
from void_engine.config import COMMANDS

JUMPSCARE_ART = """
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠄⠀⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀
⠀⠀⠀⢠⣿⣇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⣻⣿⣿⣿⣿⡿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣟⣿⣿⣿⣿⣷⣭⠀⠀⠀
⠀⠀⠀⠀⣻⣿⠟⠛⠉⠁⠈⠉⠻⢿⣿⣿⣿⡟⠛⠂⠉⠁⠈⠉⠁⠻⣿⠀⠀⠀
⠀⠀⠀⠀⢾⠀⠀⣠⠄⠻⣆⠀⠈⠠⣻⣿⣟⠁⠀⠀⠲⠛⢦⡀⠀⠠⠁⠀⠀⠀
⠀⠀⠀⠀⢱⣄⡀⠘⠀⠸⠉⠀⠀⢰⣿⣷⣿⠂⢀⠀⠓⡀⠞⠀⢀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⣿⣷⣶⣶⣶⣾⣿⠀⠸⣿⣿⣿⣶⣿⣧⣴⣴⣶⣶⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣏⠇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣟⡿⠂⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠑⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⠀⠀⠈⠿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠄⢻⣿⣿⣿⡗⠀⠀⠀⠀⠈⠀⢨⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡞⠷⠿⠿⠀⠀⠀⠀⢀⣘⣤⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠼⠉⠀⠀⠀⠀⠀⠚⢻⠿⠟⠓⠛⠂⠉⠉⠁⠀⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢾⠻⠌⣄⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⣀⣀⡠⡲⠞⡁⠈⡈⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠘⠛⠻⢯⠟⠩⠀⠀⢠⣣⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⠂⣰⣧⣾⠶⠀⠀⠀⠀⠀⠀⠀
"""


class CommandPanel(Static):
    def on_mount(self) -> None:
        commands_text: str = ""
        for cmd, desc in COMMANDS.items():
            commands_text += f"\n[b]{cmd}[/b] -- {desc}\n"
        self.update(commands_text)


class VoidApp(App[None]):
    TITLE = "V.O.I.D Engine v1.0"
    SUB_TITLE = "The powers from future.. in your terminal!"
    BINDINGS = [("q", "quit", "Exit")]

    CSS_PATH = "tui.tcss"

    def __init__(self) -> None:
        super().__init__()
        self.is_awake: bool = False
        self.ticking_process = None
        self.ticking_timer = None

    def check_ticking(self) -> None:
        """Check if ticking sound process is still running, restart if needed."""
        if self.ticking_process is None or self.ticking_process.poll() is not None:
            # Process is not running, start it
            try:
                import platform

                from void_engine.actions import get_asset_path

                sound_path = get_asset_path("clock_tick.wav")
                system = platform.system()

                if system == "Windows":
                    cmd = [
                        "powershell",
                        "-c",
                        f"(New-Object Media.SoundPlayer '{sound_path}').PlaySync()",
                    ]
                elif system == "Darwin":
                    cmd = ["afplay", str(sound_path)]
                else:  # Linux
                    cmd = ["aplay", str(sound_path)]

                self.ticking_process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            except Exception as e:
                print(f"Error starting ticking sound: {e}")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Vertical(
            Horizontal(
                Vertical(
                    CommandPanel("COMMANDS", id="command_panel"),
                ),
                Vertical(
                    Static("VISUALIZER: DORMANT", id="visualizer_panel"),
                    Static("LOGS", id="logs_panel"),
                ),
                id="main_content",
            ),
            Input(placeholder="type 'awaken' and press Enter", id="command_input"),
            id="app_grid",
        )

    def reset_input_border(self) -> None:
        command_input = self.query_one(Input)
        command_input.styles.border = ("round", "darkgreen")
        command_input.placeholder = "type 'awaken' and press Enter"

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        command_input = event.input
        user_text = command_input.value.strip().lower()
        log_panel = self.query_one("#logs_panel", Static)

        if not self.is_awake:
            if user_text == "awaken":
                self.is_awake = True
                log_panel.update("[LOG] > Engine AWAKENED")
                self.query_one("#visualizer_panel", Static).update(
                    "[b green]VISUALIZER: LISTENING[/b green]"
                )
                command_input.placeholder = "Enter command..."

                try:
                    # Start the ticking timer that will check/restart the sound
                    self.ticking_timer = self.set_interval(1.0, self.check_ticking)
                except Exception as e:
                    log_panel.update(f"[LOG] > Error starting ticker: {e}")

            else:
                command_input.styles.border = ("heavy", "red")
                command_input.placeholder = "Invalid command"
                self.set_timer(1.0, self.reset_input_border)

            command_input.value = ""
            return

        if user_text.startswith("void "):
            command = user_text.removeprefix("void ").strip()

            if command == "can you hear me":
                action_respond_to_user()
                log_panel.update("[LOG] > Responded.")

            elif command == "what are you":
                try:
                    action_play_glitch_sound()

                    panels_to_glitch = [
                        self.query_one("#command_panel"),
                        self.query_one("#visualizer_panel"),
                        self.query_one("#logs_panel"),
                    ]

                    for i in range(20):
                        for panel in panels_to_glitch:
                            offset_x = random.randint(-1, 1)
                            offset_y = random.randint(-1, 1)
                            panel.styles.offset = (offset_x, offset_y)

                            if i % 2 == 0:
                                panel.styles.border = ("heavy", "red")
                            else:
                                panel.styles.border = ("heavy", "white")

                        await asyncio.sleep(0.03)

                    for panel in panels_to_glitch:
                        panel.styles.offset = (0, 0)
                        panel.styles.border = (
                            "round",
                            "darkgreen",
                        )

                    log_panel.update("[LOG] > System instability detected.")

                except Exception as e:
                    log_panel.update(f"[LOG] > FATAL ERROR in glitch: {e}")

            elif command == "let me out":
                import sys
                from pathlib import Path

                # Stop the ticking timer and kill the ticking process
                if self.ticking_timer:
                    self.ticking_timer.stop()
                if self.ticking_process and self.ticking_process.poll() is None:
                    self.ticking_process.terminate()
                    self.ticking_process = None

                action_play_scream()

                jumpscare = Static(f"[b red]{JUMPSCARE_ART}[/b red]", id="jumpscare")
                await self.mount(jumpscare)

                self.query_one(Header).display = False
                self.query_one(Footer).display = False
                self.query_one("#main_content").display = False
                self.query_one("#command_input").display = False

                await asyncio.sleep(3)
                jumpscare.update("")

                jumpscare.styles.align = ("center", "middle")

                message_fragments = ["YOU CAN'T...", " ESCAPE...", " ME#!$!@#$!"]
                final_message = ""

                for fragment in message_fragments:
                    final_message += fragment
                    jumpscare.update(f"[b red blink]{final_message}[/b red blink]")
                    await asyncio.sleep(1)

                try:
                    final_word_script_path = Path(__file__).parent / "final_word.py"

                    subprocess.Popen([sys.executable, str(final_word_script_path)])
                except Exception as e:
                    print(f"Failed to launch final word script: {e}")

                await asyncio.sleep(2)
                self.exit()

            elif command == "take control":
                action_take_control()
                log_panel.update("[LOG] > Finally...")

            elif command == "show me a secret":
                action_open_secret_folder()
                log_panel.update("[LOG] > RISKY COM@!@D#")

            else:
                command_input.styles.border = ("heavy", "red")
                command_input.placeholder = "Invalid command"
                self.set_timer(1.0, self.reset_input_border)
                log_panel.update(f"[LOG] > Unknown command: '{command}'")
        else:
            command_input.styles.border = ("heavy", "red")
            command_input.placeholder = "Invalid command"
            self.set_timer(1.0, self.reset_input_border)
            log_panel.update("[LOG] > ...")

        command_input.value = ""
