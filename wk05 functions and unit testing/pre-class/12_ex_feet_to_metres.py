# Example: Function to convert a distance from feet and inches to metres and return the result

def convert_to_metres(feet, inches):
    return (feet*12 + inches) * 0.0254

if __name__ == "__main__":
    print(f"Equivalent distance in metres is: {convert_to_metres(6, 2.5):.2f}m")

    distance_in_metres = convert_to_metres(29, 2.5)
    print(distance_in_metres)