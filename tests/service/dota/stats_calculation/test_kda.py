import pandas as pd

from stats_app.service.dota.stats_calculation.kills_deaths_assists import get_player_max_min_avg_kda


def test_kda_no_errors():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        [1, 10, 0, 10, 0, True],
        [2, 10, 0, 0, 1, True]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_max_min_avg_kda(df) == (20, 10, 15)


def test_kda_calculation_empty():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = []
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_max_min_avg_kda(df) == (0, 0, 0)


def test_kda_invalid_dataframe():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        [1, 'LL', 1, 10, 0, True],
        [2, 10, 0, 0, 1, True]
    ]
    df = pd.DataFrame(data=data, columns=headers)

    try:
        get_player_max_min_avg_kda(df)
        assert False
    except Exception as e:
        assert True


def test_kda_zero_kda():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        [1, 0, 0, 0, 0, True],
        [1, 1, 0, 0, 1, False],
        [1, 2, 0, 0, 1, False],
        [1, 3, 0, 0, 1, False],
        [1, 4, 0, 0, 0, False]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_max_min_avg_kda(df) == (0, 0, 0)


def test_kda_zero_deaths():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        [1, 10, 0, 0, 0, True],
        [1, 1, 0, 0, 1, False],
        [1, 2, 0, 0, 1, False],
        [1, 3, 0, 0, 1, False],
        [1, 4, 0, 0, 0, False]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_max_min_avg_kda(df) == (10, 10, 10)


def test_kda_only_deaths():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        [1, 0, 10, 0, 0, True],
        [1, 1, 0, 0, 1, False],
        [1, 2, 0, 0, 1, False],
        [1, 3, 0, 0, 1, False],
        [1, 4, 0, 0, 0, False]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_max_min_avg_kda(df) == (0, 0, 0)


def test_kda_only_assists():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        [1, 0, 0, 5, 0, True],
        [1, 1, 0, 0, 1, False],
        [1, 2, 0, 0, 1, False],
        [1, 3, 0, 0, 1, False],
        [1, 4, 0, 0, 0, False]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_max_min_avg_kda(df) == (5, 5, 5)
