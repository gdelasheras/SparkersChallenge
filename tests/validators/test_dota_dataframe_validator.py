import pandas as pd

from stats_app.validators.dota_dataframe_validator import validate_dota_dataframe


def test_valid_dota_dataframe():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        [1, 10, 0, 10, 0, True],
        [2, 10, 0, 0, 1, True]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    validate_dota_dataframe(df)


def test_valid_dota_dataframe_empty():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = []
    df = pd.DataFrame(data=data, columns=headers)
    validate_dota_dataframe(df)


def test_invalid_match_id_type():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            ['a', 10, 0, 10, 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_match_id_negative():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [-1, 10, 0, 10, 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_kills_type():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, '10', 0, 10, 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_kills_negative():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, -1, 0, 10, 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_deaths_type():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, 10, '0', 10, 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_deaths_negative():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, 10, -1, 10, 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_deaths_type():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, 10, '0', 10, 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_deaths_negative():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, 10, -1, 10, 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_assists_type():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, 10, 0, '10', 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_assists_negative():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, 10, 1, -10, 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_side_type():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, 10, 0, 10, 'p', True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_side_negative():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, 10, 1, -10, 0, True],
            [2, 10, 0, 0, -1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_side_out_of_bounds():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, 10, 1, -10, 10000, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True


def test_invalid_player_type():
    try:
        headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
        data = [
            [1, 10, 0, 10, 0, True],
            [2, 10, 0, 0, 1, True]
        ]
        df = pd.DataFrame(data=data, columns=headers)
        validate_dota_dataframe(df)
        assert False
    except Exception as e:
        assert True
