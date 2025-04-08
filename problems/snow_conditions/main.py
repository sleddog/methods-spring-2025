import sys

def snow_conditions(temp: int) -> str:
    if temp < 10:
        return "Powder Snow"
    elif 10 <= temp <= 32:
        return "Packed Snow"
    else:
        return "Slushy Snow"

def main(args):
    if len(args) > 1:
        command = int(args[1])
        print(snow_conditions(command))

    else:
        print("Must give temperature")


main(sys.argv)
