def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    # Get rid of whitespace and generate reversed phrase
    phrase = phrase.replace(" ", "")
    reversed_phrase = phrase[::-1]

    # Returns True if phrases are identical, returns false otherwise
    # Handles case sensitivity
    return reversed_phrase.lower() == phrase.lower()