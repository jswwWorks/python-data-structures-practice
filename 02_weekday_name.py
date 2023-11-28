# Global constant of days of the week
DAYS_LIST = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
            ]



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

    # Adjust for indexed position
    return DAYS_LIST[day_of_week - 1]