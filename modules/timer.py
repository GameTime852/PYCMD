from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn
import time

def timer():
    console = Console()

    # Konfigurujemy białe style dla paska i procentów
    with Progress(
        TextColumn("[white]{task.description}"), # Biały opis
        BarColumn(
            style="grey37",              # Kolor "tła" paska (lekko szary, by było go widać)
            complete_style="white",      # Kolor wypełnienia paska
            finished_style="bold white"  # Kolor paska po zakończeniu
        ),
        TaskProgressColumn(text_format="[bold white]{task.percentage:>3.0f}%"), # Białe procenty
        console=console
    ) as progress:
        
        task = progress.add_task("Uruchamianie PyCMD...", total=100)
        
        while not progress.finished:
            time.sleep(0.02)
            progress.update(task, advance=1)