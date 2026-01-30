import subprocess
import os
import info
import Start
import load_exit2
import time

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
    # first = lines[1]



if not started == "started = true\n":

    Start.start()

    with open('config.txt', 'w', encoding='utf-8') as f:
        f.write("started = true\n")
        f.write(lines[1])






    
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
            f.write(lines[1])

        exit()
    elif command.lower() == "help":
        subprocess.run(["python", "help.py"])
    elif command.lower() == "about":
        info.info()
    elif command.lower() == "clear":
        os.system("cls")
    elif command.lower() == "cd":
        cel = input(r"Podaj ścieżkę katalogu (w formacie C:\...): ")
        os.system("cd " + cel)
    elif command.lower() == "ls":
        cel = input(r"Podaj ścieżkę katalogu w formacie C:\... (naciśnij Enter dla bieżącego katalogu): ")
        if cel == "":   
            cel = current_directory
        for item in os.listdir(cel):
            print(item)
    else:
        print("Nieznane polecenie. Wpisz 'help' aby uzyskać pomoc.")
    
    print("\n")