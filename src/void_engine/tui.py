from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static

from void_engine.config import COMMANDS


class CommandPanel(Static):
    def on_mount(self) -> None:
        commands: str = ""
        for cmd in COMMANDS:
            commands += f"\n{cmd} ----- {COMMANDS[cmd]}\n"
        self.update(commands)


class VoidApp(App[None]):
    TITLE = "V.O.I.D Engine v1.0"
    SUB_TITLE = "The powers from future.. in your terminal!"
    BINDINGS = [("q", "exit_app", "Exit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield CommandPanel(id="command-panel")
        yield Static("Visualizer")
        yield Static("Logs")


if __name__ == "__main__":
    app = VoidApp()
    app.run()
