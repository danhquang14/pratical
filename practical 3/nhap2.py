def main():
    MENU="C-convert celsius to fahrenheit\nF-convert Fahrenheit to Celsius\nQ-Quit"
    print(MENU)
    choice = input("Please enter:")
    while choice.upper() != "Q":
        if choice.upper() == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convertC_to_F(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice.upper()== "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_F_to_C(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
def convert_C_to_F(celsius):
   return celsius * 9.0 / 5 + 32
def convert_F_to_C(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)