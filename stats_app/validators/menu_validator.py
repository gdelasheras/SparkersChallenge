def validate_digit_menu_option(option: str, option_lst: tuple) -> int:
    """
    Validates the param 'option'. It needs to be an integer and a valid option.
    Otherwise, it throws an exception.

    :param option: Option value.
    :param option_lst: Options allowed.
    :return: The validated value as integer.
    """
    if option is not None and option.isdigit():
        option = int(option)
        if option_lst is not None and option in option_lst:
            return option
        else:
            raise Exception("Option not in the list")
    else:
        raise Exception("Invalid option")


def validate_positive_number(value: str, max_number: int) -> int:
    """
    Validates the param 'option'. It needs to be a positive integer and less than 'max_number'.
    Otherwise, it throws an exception.

    :param value: Value to validate.
    :param max_number: Maximum value.
    :return: The validated value as integer.
    """
    if value is not None and value.isdigit():
        value = int(value)
        if max_number is not None and 0 < value < max_number:
            return value
        else:
            raise Exception("Option out of bounds")
    else:
        raise Exception("Invalid option")
