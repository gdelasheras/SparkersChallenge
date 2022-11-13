import pandas as pd

from stats_app.service.dota.stats_calculation.kill_participation import get_player_kill_participation


def test_kp_no_errors():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        [1, 10, 0, 10, 0, False],
        [1, 0, 0, 0, 1, False],
        [1, 10, 0, 0, 1, True],
        [2, 20, 0, 0, 1, False],
        [2, 0, 0, 0, 1, True]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_kill_participation(df) == (100, 0, 50)


def test_kp_calculation_empty():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = []
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_kill_participation(df) == (0, 0, 0)


def test_kp_bad_dataframe():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        [1, 'LL', 1, 10, 0, True],
        [2, 10, 0, 0, 1, True]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    try:
        get_player_kill_participation(df)
        assert False
    except Exception as e:
        assert True


def test_kp_33_percent():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        # Game 1
        [1, 2, 0, 1, 0, True],
        [1, 6, 0, 1, 0, False],
        [1, 1, 1, 1, 0, False],
        [1, 0, 3, 1, 0, False],
        [1, 0, 4, 1, 0, False],
        # Enemy team
        [1, 1, 0, 0, 1, False],
        [1, 1, 0, 0, 1, False],
        [1, 2, 0, 0, 1, False],
        [1, 3, 0, 0, 1, False],
        [1, 4, 0, 0, 1, False],

        # Game 2
        [2, 2, 0, 1, 0, True],
        [2, 6, 0, 1, 0, False],
        [2, 1, 1, 1, 0, False],
        [2, 0, 3, 1, 0, False],
        [2, 0, 4, 1, 0, False],
        # Enemy team
        [2, 1, 0, 0, 1, False],
        [2, 1, 0, 0, 1, False],
        [2, 2, 0, 0, 1, False],
        [2, 3, 0, 0, 1, False],
        [2, 4, 0, 0, 1, False]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_kill_participation(df) == (33.33, 33.33, 33.33)


def test_kp_0_percent():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        # Game 1
        [1, 0, 0, 0, 0, True],
        [1, 6, 0, 1, 0, False],
        [1, 1, 1, 1, 0, False],
        [1, 0, 3, 1, 0, False],
        [1, 0, 4, 1, 0, False],
        # Enemy team
        [1, 1, 0, 0, 1, False],
        [1, 1, 0, 0, 1, False],
        [1, 2, 0, 0, 1, False],
        [1, 3, 0, 0, 1, False],
        [1, 4, 0, 0, 1, False]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_kill_participation(df) == (0, 0, 0)


def test_kp_0_percent_only_deaths():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        # Game 1
        [1, 0, 6, 0, 0, True],
        [1, 6, 0, 1, 0, False],
        [1, 1, 1, 1, 0, False],
        [1, 0, 3, 1, 0, False],
        [1, 0, 4, 1, 0, False],
        # Enemy team
        [1, 1, 0, 0, 1, False],
        [1, 1, 0, 0, 1, False],
        [1, 2, 0, 0, 1, False],
        [1, 3, 0, 0, 1, False],
        [1, 4, 0, 0, 1, False]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_kill_participation(df) == (0, 0, 0)


def test_kp_98_percent():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = [
        # Game 1
        [1, 0, 6, 98, 0, True],
        [1, 50, 0, 1, 0, False],
        [1, 50, 1, 1, 0, False],
        [1, 0, 3, 1, 0, False],
        [1, 0, 4, 1, 0, False],
        # Enemy team
        [1, 1, 0, 0, 1, False],
        [1, 1, 0, 0, 1, False],
        [1, 2, 0, 0, 1, False],
        [1, 3, 0, 0, 1, False],
        [1, 4, 0, 0, 1, False]
    ]
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_kill_participation(df) == (98, 98, 98)
