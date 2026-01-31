with open('config.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    started = lines[0]
    # first = lines[1]
    version_all = lines[1]

version = version_all[10:]

def info():

    print(f"PyCMD Wersja {version.strip()}")
    print("Autor: JacobDev")