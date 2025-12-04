# Purpose: sort hexadecimal rgb codes in numerical order
# Example of: user-defined key function with .sort()

def calc_brightness(colour):
    """
    Calculate the perceptual brightness of a colour in hexadecimal format.

    Parameters
    ----------
    colour : str
        A string containing the hexadecimal representation of a colour in rgb format.

    Returns
    -------
    float
        The perceptual brightness of the colour as a decimal.

    """
    r_value = int(colour[1:3], 16) # take first 2 hex values & convert to int
    g_value = int(colour[3:5], 16) # take middle 2 hex values & convert to int
    b_value = int(colour[5:7], 16) # take last 2 hex values & convert to int
    # calculate perceptual brightness (between 0 and 255)
    return 0.299*r_value + 0.587*g_value + 0.114*b_value 

if __name__ == "__main__":
    # list of rgb colour codes for the colours of the rainbow
    colours = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"]
    colours.sort(key=calc_brightness)
    print(colours)  