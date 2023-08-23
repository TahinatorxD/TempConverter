Fahrenheit = 0
Celsius = 0

Selection = input("Select Conversion Type\n"
                  "A. Fahrenheit to Celsius\n"
                  "B. Celsius to Fahrenheit\n"
                  "Select A or B:- ")
if Selection == 'A':
    F_C = input("Enter Temperature in Fahrenheit: ")
    if F_C.isnumeric():
        Celsius = 5/9 * (int(F_C) - 32)
        Rounded_Celsius = round(Celsius, 2)
        print(f"The Conversion of {F_C} Fahrenheit in Celsius = {Rounded_Celsius}")
    else:
        print("Invalid Character!!!\n"
              "Please Enter A Number.")

if Selection == 'B':
    C_F = input("Enter Temperature in Celsius: ")
    if C_F.isnumeric():
        Fahrenheit = int(C_F) * (9/5) + 32
        Rounded_Fahrenheit = round(Fahrenheit, 2)
        print(f"The Conversion of {C_F} Celsius in Fahrenheit = {Rounded_Fahrenheit}")
    else:
        print("Invalid Character!!!\n"
              "Please Enter A Number.")

else:
    print("You can only select from A or B")