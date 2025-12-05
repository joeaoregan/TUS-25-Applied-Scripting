from string import ascii_lowercase

def dict_from_file(filename):
    letter_freq = {}
    percentages = {}
    with open(filename) as file:
        book = file.read()

        for char in ascii_lowercase:
            letter_freq[char] = book.lower().count(char)
        
        total = sum(letter_freq.values())

        for char in letter_freq:
            percentages[char] = letter_freq[char] / total * 100

        file.close()

    return percentages


percent_frequencies = dict_from_file("Exercises\Wk9 Ex7 Dictionaries and Datetime\Carmilla.txt")
print("Letter Frequency")
for letter in sorted(percent_frequencies):
    print(f"{letter:^5}{percent_frequencies.get(letter):^9.1f}")