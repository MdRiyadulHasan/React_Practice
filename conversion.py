print("Unit Converter")
print("1. Meter to Foot")
print("2. Foot to Meter")
print("3. Meter to Centimeter")
print("4. Centimeter to Meter")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    meter = float(input("Enter value in meter: "))
    foot = meter * 3.28084
    print("Foot =", foot)

elif choice == 2:
    foot = float(input("Enter value in foot: "))
    meter = foot / 3.28084
    print("Meter =", meter)

elif choice == 3:
    meter = float(input("Enter value in meter: "))
    cm = meter * 100
    print("Centimeter =", cm)

elif choice == 4:
    cm = float(input("Enter value in centimeter: "))
    meter = cm / 100
    print("Meter =", meter)

else:
    print("Invalid Choice")