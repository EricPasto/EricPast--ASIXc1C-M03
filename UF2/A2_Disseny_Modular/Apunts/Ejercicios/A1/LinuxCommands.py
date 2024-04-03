import random

# Frases de benvinguda aleatòries
welcome_messages = [
    "Benvingut al simulador de sistema operatiu Linux!",
    "Hola! Aquest és el teu sistema operatiu Linux virtual.",
    "Ara estàs interactuant amb un sistema operatiu simulat de tipus Linux."
]

# Funció per imprimir una frase de benvinguda aleatòria
def print_welcome_message():
    print(random.choice(welcome_messages))

# Funció per mostrar missatge d'error per opcions no vàlides
def print_invalid_option_error(option):
    print(f"Value {option} is not valid option BACALAO")

# Funció per mostrar l'ajuda
def print_help(command):
    if command == 'touch':
        print("touch is used to create an empty file.")
    elif command == 'grep':
        print("grep is used to search for text patterns in files.")
    elif command == 'cat':
        print("cat is used to concatenate files and print on the standard output.")
    elif command == 'fdisk':
        print("fdisk is a dialog-driven program for creation and manipulation of partition tables.")
        print("It understands GPT, MBR, Sun, SGI and BSD partition tables.")
        print("Block devices can be divided into one or more logical disks called partitions.")
        print("This division is recorded in the partition table, usually found in sector 0 of the disk.")
        print("(In the BSD world one talks about 'disk slices' and a 'disklabel'.)")
    elif command == 'cmp':
        print("cmp is used to compare two files byte by byte.")
    elif command == 'dmesg':
        print("dmesg is used to print and control the kernel ring buffer.")
    elif command == 'man':
        print("man is used to display the manual pages of Unix-like operating systems.")
    elif command == 'top':
        print("top is a command-line tool that allows you to monitor system processes.")
    elif command == 'htop':
        print("htop is an interactive process viewer for Unix systems.")
    elif command == 'halt':
        print("halt is used to stop the system, though it will not power it off.")
    else:
        print(f"{command} command not found, 'User BACALAO'")

# Funció per mostrar la versió
def print_version(command):
    if command == 'fdisk':
        print("v0.1")
    else:
        print(f"No version available for {command}")

# Funció principal
def main():
    print_welcome_message()

    # Mapa de comandes amb opcions vàlides
    commands = {
        'touch': ['-h', '--help'],
        'grep': ['-h', '--help'],
        'cat': ['-h', '--help'],
        'fdisk': ['-h', '--help', '-v', '--version'],
        'cmp': ['-h', '--help'],
        'dmesg': ['-h', '--help'],
        'man': ['-h', '--help'],
        'top': ['-h', '--help'],
        'htop': ['-h', '--help'],
        'halt': ['-h', '--help']
    }

    # Llegir l'entrada de l'usuari
    user_input = input("Introdueix una comanda: ")

    # Separar l'entrada en comanda i opcions
    parts = user_input.split()
    command = parts[0]
    options = parts[1:]

    # Comprovar si la comanda és vàlida i gestionar opcions
    if command in commands:
        if not options:
            print(f"{command} needs one parameter. For instance -v or -h")
        else:
            for option in options:
                if option in commands[command]:
                    if option in ['-h', '--help']:
                        print_help(command)
                    elif option in ['-v', '--version']:
                        print_version(command)
                else:
                    print_invalid_option_error(option)
    else:
        print(f"{command} command not found, 'User BACALAO'")

# Executar el programa
if __name__ == "__main__":
    main()
