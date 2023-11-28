def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """


    return {ltr: phrase.count(ltr) for ltr in phrase}


    # Simple solution (generic frequency counter):

    # letter_frequency = {}

    # # Generate frequency counter
    # for letter in phrase:
    #     if letter in letter_frequency:
    #         letter_frequency[letter] += 1
    #     else:
    #         letter_frequency[letter] = 1

    # return letter_frequency


