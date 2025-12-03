def camel_to_snake(identifier):
    snake_name = ""
    for char in identifier:
        if char.isupper():
            if snake_name:
                snake_name += '_'
            snake_name += char.lower()
        else:
            snake_name += char
    return snake_name