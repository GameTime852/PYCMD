import subprocess
import os
import info
import Start

os.system("cls")
info.info()
# Uruchomienie innego skryptu .py

Start.start()

# Pobranie i wyświetlenie bieżącego katalogu

while True: 
    print("\n")
    current_directory = os.getcwd()
    command = input(current_directory+"> ")

    if command.lower() == "exit":
        os.system("cls")
        print("!")
    elif command.lower() == "help":
        subprocess.run(["python", "help.py"])
    elif command.lower() == "about":
        subprocess.run(["python", "info.py"])
    elif command.lower() == "clear":
        os.system("cls")
    elif command.lower() == "cd":
        cel = input("Podaj ścieżkę katalogu: ")
        os.system("cd " + cel)
    elif command.lower() == "ls":
        cel = input("Podaj ścieżkę katalogu (naciśnij Enter dla bieżącego katalogu): ")
        if cel == "":   
            cel = current_directory
        for item in os.listdir(cel):
            print(item)