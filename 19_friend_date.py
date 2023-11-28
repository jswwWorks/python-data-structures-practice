def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """

    # Grab hobbies for each friend
    friend_one_hobbies = a[2]
    friend_two_hobbies = b[2]


    # Intersection between sets
    hobbies_in_common = set(friend_one_hobbies) & set(friend_two_hobbies)


    # Return true if they have hobbies in common, otherwise return false
    if hobbies_in_common:
        return True
    else:
        return False
