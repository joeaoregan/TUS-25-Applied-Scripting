# 

def calc_brightness(colour):
    r_value = int(colour[1:3], 16)
    g_value = int(colour[3:5], 16)
    b_value = int(colour[5:7], 16)
    # calculate perceptual brightness (between 0 and 255)
    return 0.299*r_value + 0.587*g_value + 0.114*b_value

rainbow_colours = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"]

rainbow_colours.sort(key=calc_brightness)
print(rainbow_colours)