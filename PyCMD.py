import subprocess
import os
import modules.info as info
import modules.Start as Start
import modules.load_exit2 as load_exit2
import time
import modules.help as help


def clear():
    os.system("cls")
def wait(seconds):
    time.sleep(seconds)


os.system("cls")
info.info()
# Uruchomienie innego skryptu .py
with open('config.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    started = lines[0]
    # first = lines[2]


if not started == "started = true\n":

    Start.start()

    with open('config.txt', 'w', encoding='utf-8') as f:
        f.write("started = true\n")
        f.write(lines[0])


#if first == "first = true\n":
 #   print("Witaj w PyCMD!")

# Pobranie i wyświetlenie bieżącego katalogu

while True: 
    print("\n")
    current_directory = os.getcwd()
    command = input(current_directory+"> ")

    if command.lower() == "exit":
        os.system("cls")
        load_exit2.load_exit()
        with open('config.txt', 'w', encoding='utf-8') as f:
            f.write("started = false\n")
            f.write(lines[0])

        exit()
    elif command.lower() == "help":
        page = int(input("Podaj numer strony pomocy (domyślnie 1): ") or "1")
        help.help(page)
    elif command.lower() == "about":
        info.info()
    elif command.lower() == "clear":
        os.system("cls")
    elif command.lower() == "cd":
        cel = input(r"Podaj ścieżkę katalogu (w formacie C:\...): ")
        os.chdir(cel)
    elif command.lower() == "ls":
        cel = input(r"Podaj ścieżkę katalogu w formacie C:\... (naciśnij Enter dla bieżącego katalogu): ")
        if cel == "":   
            cel = current_directory
        for item in os.listdir(cel):
            print(item)
    elif command.lower() == "pwd":
        print(current_directory)
    elif command.lower() == "status":
        stat = input("Podaj status do ustawienia (on/off): ")
        if stat == "on":
            with open('config.txt', 'w', encoding='utf-8') as f:
                f.write("started = true\n")
                f.write(lines[1])
            print("Status ustawiony na ON.")
        elif stat == "off":
            with open('config.txt', 'w', encoding='utf-8') as f:
                f.write("started = false\n")
                f.write(lines[1])
            print("Status ustawiony na OFF.")
        else:
            print("Nieprawidłowa wartość statusu. Użyj 'on' lub 'off'.")

    else:
        print(f"Nieznane polecenie: {command}. Wpisz 'help' aby uzyskać pomoc.")
    
    print("\n")
