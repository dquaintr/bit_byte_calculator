##Bit Byte calculator

a = float(input("Please enter amount: "))
unit = input("Please enter unit: Byte, Kilobyte, Megabyte, Gigabyte, Terabyte etc.,"
             " Bit, Kilobit, Megabit, Gigabit, Terabit etc. , Kibibit,Mebibit,Gibibit, etc. "
             "Kibibyte, Mebibyte etc.: ")

if "yte" in unit:
    x = a * 8
    answer = unit.replace("yte", "it")
    print(f"{a} {unit} is equal to {x} {answer}.")
elif "it" in unit:
    x = a/8
    answer = unit.replace("it","yte")
    print(f"{a} {unit} is equal to {x} {answer}.")
else:
    print("Please enter one of the units in the style above.")



