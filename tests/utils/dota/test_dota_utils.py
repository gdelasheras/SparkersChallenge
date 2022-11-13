from stats_app.utils.dota.dota_utils import get_team_side, TEAM_DIRE, TEAM_RADIANT


def valid_team_side_radiant():
    team = get_team_side('1')
    assert team == TEAM_RADIANT


def valid_team_side_dire():
    team = get_team_side('0')
    assert team == TEAM_DIRE


def valid_team_side_radiant_as_int():
    team = get_team_side(1)
    assert team == TEAM_RADIANT


def valid_team_side_dire_as_int():
    team = get_team_side(0)
    assert team == TEAM_DIRE


def test_team_invalid():
    try:
        get_team_side('RADIANT')
        assert False
    except Exception as e:
        assert True
        assert "Invalid player_slot" in str(e)


def test_team_invalid_number():
    try:
        get_team_side(100)
        assert False
    except Exception as e:
        assert True
        assert "Invalid player_slot" in str(e)