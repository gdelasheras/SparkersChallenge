from stats_app.validators.menu_validator import validate_digit_menu_option, validate_positive_number


def test_valid_num_option():
    option = validate_digit_menu_option('1', (1, 2))
    assert option == 1


def test_valid_num_option_as_num_type():
    option = validate_digit_menu_option('1', (1, 2))
    assert option == 1


def test_option_not_in_list():
    try:
        validate_digit_menu_option('1', ())
        assert False
    except Exception as e:
        assert True
        assert "Option not in the list" in str(e)


def test_invalid_option():
    try:
        validate_digit_menu_option('OPTION', ())
        assert False
    except Exception as e:
        assert True
        assert "Invalid option" in str(e)


def test_empty_option():
    try:
        validate_digit_menu_option(None, ())
        assert False
    except Exception as e:
        assert True
        assert "Invalid option" in str(e)


def test_empty_option_list():
    try:
        validate_digit_menu_option('1', None)
        assert False
    except Exception as e:
        assert True
        assert "Option not in the list" in str(e)


def test_valid_positive_number():
    option = validate_positive_number('1', 10)
    assert option == 1


def test_invalid_number():
    try:
        validate_positive_number('OPTION', 10)
        assert False
    except Exception as e:
        assert True
        assert "Invalid option" in str(e)


def test_invalid_max_number():
    try:
        validate_positive_number('1', None)
        assert False
    except Exception as e:
        assert True
        assert "Option out of bounds" in str(e)


def test_number_out_of_bounds():
    try:
        validate_positive_number('20', 10)
        assert False
    except Exception as e:
        assert True
        assert "Option out of bounds" in str(e)


def test_empty_number():
    try:
        validate_positive_number(None, 10)
        assert False
    except Exception as e:
        assert True
        assert "Invalid option" in str(e)
