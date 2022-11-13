import pandas as pd

from stats_app.service.dota.stats_calculation.kill_participation import get_player_kill_participation


def test_kda_no_errors():
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


def test_kda_calculation_empty():
    headers = ['match_id', 'kills', 'deaths', 'assists', 'side', 'player']
    data = []
    df = pd.DataFrame(data=data, columns=headers)
    assert get_player_kill_participation(df) == (0, 0, 0)


def test_kda_bad_dataframe():
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
