from string import ascii_lowercase

def is_pangram(phrase):
    """
    Check if a phrase is a pangram (uses every letter of the alphabet at least once).
    
    Parameters
    ----------
    phrase : str
        A phrase to check for every letter in the alphabet.
    
    Returns
    -------
    boolean
        If the phrase contains every letter.
    
    Examples
    --------
    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram("The quick brown fox jumps over a dog")
    False
    """
    str = ascii_lowercase
    for letter in phrase:
        if letter.isalpha():
            if letter.lower() in str:
                str = str.replace(letter.lower(), "")
                # print(str, len(str))

        if len(str) == 0:
            return True

    # print(str)
    return False


def is_palindrome(phrase, perfect=False):
    if perfect:
        return phrase.lower() == phrase[::-1].lower()
    
    temp = ""
    for letter in phrase:
        if letter.isalpha():
            temp += letter.lower()

    # print(temp)
    # phrase = phrase.lower().replace(" ", "")
    # return phrase == phrase[::-1]
    return temp == temp[::-1]


if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)

    # print()
    # # print(check_pangram("abcdefghijklmnopqrstuvwxyz"))
    # print(is_pangram("The quick brown fox jumps over the lazy dog"))
    # print(is_pangram("Sphinx of black quartz, judge my vow"))
    # print()
    # print(is_palindrome("Rats live on no evil star"))
    # print(is_palindrome("A man, a plan, a canal - Panama!", True))
    # print(is_palindrome("A man, a plan, a canal - Panama!", False))
    # print(is_palindrome("A man, a plan, a canal - Panama!"))
    
    while(True):
        phrase = input("\nEnter a word or phrase, or q to quit: ")
        
        if phrase.lower() == "q":
            break

        if is_palindrome(phrase, True):
            print("This is a perfect palindrome")
        elif is_palindrome(phrase):
            print("This is a palindrome")
        else:
            print("This is not a palindrome")

        if is_pangram(phrase):
            print("This is a pangram")
        else:
            print("This is not a pangram")
