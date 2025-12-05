from string import ascii_lowercase 

def get_percent_letter_frequencies(filename):
    with open(filename) as file:
        book = file.read()
        frequencies = {}

        for char in ascii_lowercase:
            frequencies[char] = book.lower().count(char)

        total = sum(frequencies.values())

        percentages = {}

        for char in frequencies:
            percentages[char] = frequencies[char] / total * 100

        file.close()

        return percentages
    
    
percent_frequencies = get_percent_letter_frequencies("Exercises\Wk9 Ex7 Dictionaries and Datetime\Carmilla.txt")
print("Letter Frequency")
for letter in sorted(percent_frequencies):
    print(f"{letter:^5}{percent_frequencies.get(letter):^9.1f}")