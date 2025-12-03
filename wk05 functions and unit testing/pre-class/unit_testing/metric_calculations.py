def convert_to_metres(feet, inches):
    return (feet*12 + inches) * 0.0254

def metres_to_imperial(metres):
    feet = metres * 3.28084

    whole_feet = int(feet)

    inches = (feet - whole_feet) * 12

    return whole_feet, inches