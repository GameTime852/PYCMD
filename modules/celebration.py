import random
import time
from rich.console import Console

def celebrate():
    console = Console()
    width = console.width

    # Konfiguracja konfetti
    shapes = ["🎗️", "o", "★", "🎊", "🎈", "✨", "🎉", "~"]
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white", "bright_yellow", "bright_red"]

    # Nagłówek powitalny dla wersji 1.0
    console.clear()
    console.print("\n")
    console.print("✨  [bold bright_yellow]PYCMD WERSJA 1.0[/bold bright_yellow]  ✨", justify="center")
    console.print("[italic cyan]Dziękujemy za aktualizację![/italic cyan]", justify="center")
    console.print("\n")
    time.sleep(1)

    # Animacja spadającego konfetti
    # Pętla generuje linie pełne losowych znaków
    for _ in range(5):  # Liczba klatek (długość trwania efektu)
        line = ""
        for _ in range(width):
            if random.random() < 0.35: # 10% szansy na konfetti w danym punkcie
                color = random.choice(colors)
                shape = random.choice(shapes)
                line += f"[{color}]{shape}[/]"
            else:
                line += " "
        console.print(line)
        time.sleep(0.1) # Prędkość spadania

    time.sleep(0.1)
    console.clear() # Wyczyść ekran po zakończeniu, aby przejść do programu