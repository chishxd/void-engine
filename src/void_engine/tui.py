from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class VoidApp(App):
    TITLE = "V.O.I.D Engine v1.0"
    SUB_TITLE = "The powers from future.. in your terminal!"
    BINDINGS = [("q", "exit_app", "Exit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


if __name__ == "__main__":
    app = VoidApp()
    app.run()
