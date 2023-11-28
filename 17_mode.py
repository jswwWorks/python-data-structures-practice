def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """


    # Create a dictionary and then find max value
    number_frequencies = {num: nums.count(num) for num in nums}
    highest_val = max(number_frequencies.values())
    for item in number_frequencies:
        if number_frequencies[item] == highest_val:
            return item



    # Simplest solution (iterating through a set and grabbing highest values):
    # # Placeholder values for the
    # highest_count = 0
    # highest_count_num = 0

    # num_set = set(nums)

    # for num in num_set:
    #     current_count = nums.count(num)
    #     if current_count > highest_count:
    #         highest_count = current_count
    #         highest_count_num = num

    # return highest_count_num


    # Fanciest solution:

    # # Create a dictionary and then find max value
    # number_frequencies = {num: nums.count(num) for num in nums}
    # return max(number_frequencies, key=number_frequencies.get)