marks = [84, 68, 71, 88, 95, 88]
print(marks)

marks = []
print(marks)

marks = list()
print(marks)

marks = list((84, 68, 71, 88, 95, 88))
print(marks)

port_numbers = [22, 25, 80, 443, 901] # int
users = ['root', 'apache', 'mysql', 'jbloggs'] # str
temperatures = [21.5, 19.8, 22.3, 18.7, 16.2, 10.3] # float

weather_log = [3, "sunny", 21.3, False, 18.7]
print(weather_log)

marks = [0] * 6
print(marks)

rgb_white = [255] * 3
print(rgb_white)

from string import ascii_lowercase
lowercase_letters = list(ascii_lowercase)
print(ascii_lowercase)
print(lowercase_letters)

dna_sequence = "AGCTGATCGA"
nucleotides = list(dna_sequence)
print(nucleotides)

values = list(range(10))
print(values)

odd_numbers = list(range(1,10,2))
print(odd_numbers)

quote = "Always look on the bright side of life"
print(quote.split())

comment = "Linus Torvalds, 101, 090 6424400, 090 6412345, Creator of Linux"
print(comment.split(","))

identifier = "my_impractical_variable_name"
print(identifier.split("_"))

# join()
octets_list = ['192','168','26','10']
ip_address = ".".join(octets_list)
print(ip_address)

path_parts = ['home', 'student', 'programs', 'hello.py']
file_path = "/".join(path_parts)
print(file_path)

capitalised_words = ['My', 'Impractical', 'Variabl', 'Name']
camel_name = "".join(capitalised_words)
print(camel_name)

dna_fragments = ['ATG', 'CGA', 'TTC', 'GGA']
full_sequence = "".join(dna_fragments)
print(full_sequence)

