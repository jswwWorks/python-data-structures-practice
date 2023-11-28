def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    # Handle invalid inputs
    if day_of_week <= 0 or day_of_week > 7:
        return None

    # List of weekdays
    days_list = [
                "Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday"
                ]

    # Adjust for indexed position
    return days_list[day_of_week - 1]