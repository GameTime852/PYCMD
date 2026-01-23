
from rich.console import Console
import time

def load_exit():
    
    console = Console()

    #bouncingBall (skacząca piłka)✅
    # 'spinner' to nazwa animacji. "dots" to klasyczne kropki kręcące się w kółko.
    with console.status("Zamykanie...", spinner="bouncingBall", spinner_style="white"):
        # Tutaj umieść swój kod, który zajmuje czas
        time.sleep(3)
