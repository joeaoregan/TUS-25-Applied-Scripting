def convert_to_metres(feet, inches):
    metres = (feet * 12 + inches) * 0.0254
    print(f"Equivalent distance in metres is: {metres:.2f}m")


if __name__ == "__main__":
    convert_to_metres(6, 2.5)