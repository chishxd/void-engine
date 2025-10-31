from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header, Input, Static

from void_engine.config import COMMANDS


# The widget for all commands
class CommandPanel(Static):
    def on_mount(self) -> None:
        commands: str = ""
        for cmd in COMMANDS:
            commands += f"\n[b]{cmd}[/b] -- {COMMANDS[cmd]}\n"
        self.update(commands)


# The main container
class VoidApp(App[None]):
    TITLE = "V.O.I.D Engine v1.0"
    SUB_TITLE = "The powers from future.. in your terminal!"
    BINDINGS = [("q", "exit_app", "Exit")]

    CSS_PATH = "tui.tcss"

    is_true: bool = False

    def __init__(self) -> None:
        super().__init__()

        self.is_awake: bool = False

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Vertical(
            Horizontal(
                Vertical(
                    CommandPanel("COMMANDS", id="command_panel"),
                ),
                Vertical(
                    Static("VISUALIZER", id="visualizer_panel"),
                    Static("LOGS", id="logs_panel"),
                ),
                id="main_content",
            ),
            Input(placeholder="type 'awaken' and press Enter", id="command_input"),
            id="app_grid",
        )

    def on_input_submitted(self, event: Input.Submitted):
        if event.value.lower() == "awaken":
            self.is_awake: bool = True
            self.query_one("#logs_panel", Static).update("[LOG] > Engine AWAKENED")
            self.query("#command_input").remove()


if __name__ == "__main__":
    app = VoidApp()
    app.run()
