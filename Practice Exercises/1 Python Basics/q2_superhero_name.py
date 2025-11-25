# Write a Python program which generates and displays your Superhero name, by adding your 
# favourite colour and the name your favourite animal.

# For example:

# Input	    | Result
# --------- | -----------------------------------------------
# black     | Enter the name of your favourite colour: black
# panther   | Enter the name of your favourite animal: panther
#           | Your Superhero Name is: Black Panther
# --------- | -----------------------------------------------
# red       | Enter the name of your favourite colour: red
# fox       | Enter the name of your favourite animal: fox
#           | Your Superhero Name is: Red Fox
# --------- | -----------------------------------------------
# grey      | Enter the name of your favourite colour: grey
# wolf      | Enter the name of your favourite animal: wolf
#           | Your Superhero Name is: Grey Wolf
# --------- | -----------------------------------------------
# pink      | Enter the name of your favourite colour: pink
# falcon    | Enter the name of your favourite animal: falcon
#           | Your Superhero Name is: Pink Falcon
# --------- | -----------------------------------------------
# green     | Enter the name of your favourite colour: green
# python    | Enter the name of your favourite animal: python
#           | Your Superhero Name is: Green Python


colour = input("Enter the name of your favourite colour: ")
animal = input("Enter the name of your favourite animal: ")

colour = colour.title()
animal = animal.title()

# print(f"Your Superhero Name is: {colour} {animal}")

superhero_name = colour + " " + animal
print(f"Your Superhero Name is: {superhero_name}")