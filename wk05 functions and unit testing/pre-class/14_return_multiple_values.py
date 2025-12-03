def metres_to_imperial(metres):
    feet = metres * 3.28084

    whole_feet = int(feet)

    inches = (feet - whole_feet) * 12

    return whole_feet, inches

if __name__ == "__main__":
    metres = float(input("Enter the distance in metres: "))

    feet, inches = metres_to_imperial(metres)

    print(f"Equivalent distance is {feet} feet, {inches:.1f} inches")