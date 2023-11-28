def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    answer_phrase = ''

    for letter in phrase:
        if letter.lower() == to_swap.lower():
            answer_phrase += (letter.swapcase())
        else:
            answer_phrase += letter

    return answer_phrase

