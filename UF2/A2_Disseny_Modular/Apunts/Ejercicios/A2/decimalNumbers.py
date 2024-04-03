def print_digit(digit):
    digits = {
        '0': [" ##### ",
              "#     #",
              "#     #",
              "#     #",
              "#     #",
              "#     #",
              " ##### "],
        '1': ["   #   ",
              "  ##   ",
              " # #   ",
              "   #   ",
              "   #   ",
              "   #   ",
              " ##### "],
        '2': [" ##### ",
              "#     #",
              "      #",
              " ##### ",
              "#      ",
              "#      ",
              "#######"],
        '3': [" ##### ",
              "#     #",
              "      #",
              " ##### ",
              "      #",
              "#     #",
              " ##### "],
        '4': ["#      ",
              "#    # ",
              "#    # ",
              "#######",
              "     # ",
              "     # ",
              "     # "],
        '5': ["#######",
              "#      ",
              "#      ",
              " ##### ",
              "      #",
              "#     #",
              " ##### "],
        '6': [" ##### ",
              "#     #",
              "#      ",
              " ######",
              "#     #",
              "#     #",
              " ##### "],
        '7': ["#######",
              "#    # ",
              "    #  ",
              "   #   ",
              "  #    ",
              "  #    ",
              "  #    "],
        '8': [" ##### ",
              "#     #",
              "#     #",
              " ##### ",
              "#     #",
              "#     #",
              " ##### "],
        '9': [" ##### ",
              "#     #",
              "#     #",
              " ######",
              "      #",
              "#     #",
              " ##### "],
        '-': ["       ",
              "       ",
              "       ",
              " ##### ",
              "       ",
              "       ",
              "       "]
    }

    for line in digits.get(digit, digits['-']):
        print(line)

def print_number(number):
    for line in range(7):
        for digit in number:
            print_digit(digit)
            print("  ", end="")
        print()

def main():
    while True:
        try:
            number = input("Introdueix un nombre: ")
            if not number.isdigit() and number[0] != '-':
                raise ValueError
            print_number(number)
        except ValueError:
            print("Entrada no vàlida. Introdueix un nombre enter.")

if __name__ == "__main__":
    main()
