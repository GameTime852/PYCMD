import os
import time
import importlib.util
import sys
import logging
import atexit  # <--- NOWE: Do czyszczenia przy wyjściu
from pathlib import Path

# Importy twoich modułów
import modules.help as help
import modules.info as info
import modules.Start as Start
import modules.load_exit2 as load_exit2

# --- KONFIGURACJA LOGÓW ---
# Podczas działania programu logi są zapisywane tutaj.
logging.basicConfig(
    filename='logs.txt',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
    filemode='w',
    encoding='utf-8'
)

# --- NOWE: CZYSZCZENIE LOGÓW PO ZAMKNIĘCIU ---
def clean_logs_on_exit():
    """Funkcja uruchamiana automatycznie przy zamykaniu programu."""
    logging.shutdown() # Zwalniamy plik logs.txt
    try:
        # Otwieramy plik w trybie 'w' i nic nie piszemy -> plik staje się pusty
        with open('logs.txt', 'w', encoding='utf-8') as f:
            pass 
    except Exception:
        pass

# Rejestrujemy funkcję, aby wykonała się na samym końcu
atexit.register(clean_logs_on_exit)

# --- SYSTEM MODÓW ---

mod_commands = {}

def load_mods():
    """Ładuje mody w tle, pisząc tylko do logs.txt"""
    mods_path = Path('mods')
    
    if not mods_path.exists():
        try:
            mods_path.mkdir()
        except Exception:
            pass 

    logging.info("--- START SYSTEMU ---")
    
    if not any(mods_path.iterdir()):
        logging.info("Brak modów do załadowania.")
        return

    for item in mods_path.iterdir():
        # 1. Foldery
        if item.is_dir():
            main_file = item / "main.py"
            if main_file.exists():
                try:
                    sys.path.append(str(item))
                    spec = importlib.util.spec_from_file_location(item.name, main_file)
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    
                    if hasattr(mod, 'register'):
                        mod.register(mod_commands)
                        logging.info(f"ZAŁADOWANO: {item.name}")
                    else:
                        logging.warning(f"POMINIĘTO: {item.name} (brak register)")
                except Exception as e:
                    logging.error(f"BŁĄD KRYTYCZNY w {item.name}: {e}")
                    
        # 2. Pliki .py
        elif item.suffix == ".py" and item.name != "__init__.py":
            try:
                spec = importlib.util.spec_from_file_location(item.stem, item)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                
                if hasattr(mod, 'register'):
                    mod.register(mod_commands)
                    logging.info(f"ZAŁADOWANO: {item.name}")
                else:
                    logging.warning(f"POMINIĘTO: {item.name}")
            except Exception as e:
                logging.error(f"BŁĄD KRYTYCZNY w {item.name}: {e}")

# --- FUNKCJE POMOCNICZE ---

def clear():
    os.system("cls")

# --- INICJALIZACJA ---

file_path = Path('config.txt')
if not file_path.exists():
    file_path.touch()

os.system("cls")
load_mods() 
info.info()

with open('config.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if not lines:
        lines = ["started = false\n"]
    started = lines[0]

if not started == "started = true\n":
    Start.start()
    with open('config.txt', 'w', encoding='utf-8') as f:
        f.write("started = true\n")
        if len(lines) > 1: f.writelines(lines[1:])

# --- PĘTLA GŁÓWNA ---

while True: 
    print("\n")
    current_directory = os.getcwd()
    try:
        command = input(current_directory + "> ")
    except EOFError:
        break
        
    command_lower = command.lower()
    
    logging.info(f"CMD: {command}")

    # 1. MODY
    if command_lower in mod_commands:
        try:
            mod_commands[command_lower]()
        except Exception as e:
            print(f"Błąd wykonywania polecenia: {e}")
            logging.error(f"Exception w modzie '{command_lower}': {e}")
        continue

    # 2. WBUDOWANE
    elif command_lower == "exit":
        logging.info("Zamykanie...")
        clear()
        load_exit2.load_exit()
        try:
            with open('config.txt', 'w', encoding='utf-8') as f:
                f.write("started = false\n")
                if len(lines) > 1: f.writelines(lines[1:])
        except: pass
        exit()

    elif command_lower == "help":
        val = input("Podaj numer strony (1): ")
        page = int(val) if val.isdigit() else 1
        help.help(page)

    elif command_lower == "about":
        info.info()

    elif command_lower == "clear":
        clear()

    elif command_lower == "cd":
        cel = input(r"Ścieżka (lub ..): ")
        try:
            os.chdir(cel)
            logging.info(f"CD -> {os.getcwd()}")
        except Exception as e:
            print(f"Błąd: {e}")

    elif command_lower == "ls":
        cel = input(r"Ścieżka (Enter dla obecnej): ")
        target = cel if cel else current_directory
        try:
            for item in os.listdir(target):
                print(f" - {item}")
        except Exception as e:
            print(f"Błąd: {e}")

    elif command_lower == "pwd":
        print(current_directory)

    elif command_lower == "status":
        stat = input("Status (on/off): ")
        try:
            with open('config.txt', 'w', encoding='utf-8') as f:
                f.write(f"started = {'true' if stat=='on' else 'false'}\n")
                if len(lines) > 1: f.writelines(lines[1:])
            print(f"Status: {stat}")
        except Exception: pass

    elif command.strip() == "config":
        os.system("notepad config.txt")
        
    else:
        if command.strip():
            print(f"Nieznane polecenie: {command}")
            logging.warning(f"Nieznane polecenie: {command}")