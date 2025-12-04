# Timing snake_case to camelCase Functions
from time import perf_counter
from random import choice

def snake_to_camel1(name):
    """Convert an identifier in snake_case to camelCase using s"""
    camel_name = name.replace("_", " ")
    camel_name = camel_name.title()
    camel_name = camel_name.replace(" ", "")
    # change initial letter to lowercase
    camel_name = camel_name[0].lower() + camel_name[1:]
    return camel_name

def snake_to_camel2(name):
    """Convert and identifier in snake_case to camelCase using a"""
    while "_" in name:
        # find the index of the first underscore (working left)
        under_index = name.find("_")
        # combine the part before the underscore
        # with the capitalised part after the underscore
        name = name[:under_index] + name[under_index+1:].capitalize()
    if name[0].isupper():
        name = name[0].lower() + name[1:]
    return name

def snake_to_camel3(name):
    """Convert and identifier in snake_case to camelCase using a"""
    # splitting a string creates a list of "words"
    words = name.split("_")
    # capitalise all the other words apart from the first
    for i in range(1, len(words)):
        words[i] = words[i].capitalize()
    # joining a list creates a string
    camel_name = "".join(words)
    return camel_name

def snake_to_camel4(name):
    """Convert and identifier in snake_case to camelCase using a"""
    # spliting a string creates a list of "words"
    words = name.split("_")
    # capitalise all the other words apart from the first
    # joining a list creates a string, "".join means don't sepa
    camel_name = words[0] + "".join([word.capitalize() for word in words[1:]])
    return camel_name


def time_snake_to_camel(snake_function, name_list):
    start = perf_counter()

    # Convert each name in the list from snake_case to camelCase
    for name in name_list:
        snake_function(name)

    end = perf_counter()

    return end - start

def generate_snake_case_list(size=1000000):
    """Generate 1000s of names in snake_case using 3-5 letter words from word list files"""
    word_list = []
    for filename in ["word3", "word4", "word5"]:
        with open(filename) as file_in:
            word_list.extend([ word.strip().lower() for word in file_in.readlines() ])

    # start with a number of single word names selected at random
    name_list = [choice(word_list) for i in range(size)]


    name_list.extend([choice(word_list)+"_"+choice(word_list) for word in word_list) # ?


if __name__ == "__main__":
    name_list = generate_snake_case_list()

    print("Timing snake_to_camel1 - using string methods only")
    duration1 = time_snake_to_camel(snake_to_camel1, name_list)
    print(f"Time taken: {duration1:.3f} seconds")

    print()
    print("Timing snake_to_camel2 - using a while loop")
    duration2 = time_snake_to_camel(snake_to_camel2, name_list)
    print(f"Time taken: {duration2:.3f} seconds")

    print()
    print("Timing snake_to_camel3 - using a list")
    duration2 = time_snake_to_camel(snake_to_camel3, name_list)
    print(f"Time taken: {duration2:.3f} seconds")

    print()
    print("Timing snake_to_camel4 - using a list comprehension")
    duration2 = time_snake_to_camel(snake_to_camel4, name_list)
    print(f"Time taken: {duration2:.3f} seconds")