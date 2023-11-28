import math

def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, raise error:

        >>> calculate('foo', 2, 3)
        Traceback (most recent call last):
          ...
        ValueError: Invalid Operation
    """

    answer = 0

    # Handle invalid operation inputs
    if (
        operation != "add" and
        operation != "subtract" and
        operation != "multiply" and
        operation != "divide"
       ):
        raise ValueError("Invalid Operation")

    # Perform desired operation and truncate to integer if needed
    if operation == "add":
        answer = a + b
    elif operation == "subtract":
        answer = a - b
    elif operation == "multiply":
        answer = a * b
    else:
        answer = a / b

    # If make_int is true, convert to integer
    if make_int:
        answer = math.floor(answer)

    # Return answer with message
    return (f"{message} {answer}")
