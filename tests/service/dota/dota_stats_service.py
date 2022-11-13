from stats_app.repository.dota.dota_repository import DotaRepository
from stats_app.service.dota.dota_stats_service import DotaService


def test_player_stats():
    try:
        DotaService(DotaRepository()).get_player_stats(639740, 1)
        assert True
    except Exception as e:
        assert False


def test_player_stats_bad_user_id():
    try:
        DotaService(DotaRepository()).get_player_stats(0, 1)
        assert False
    except Exception as e:
        assert True


def test_player_stats_bad_user_id_letter():
    try:
        DotaService(DotaRepository()).get_player_stats('L', 1)
        assert False
    except Exception as e:
        assert True


def test_player_stats_bad_num_matches_letter():
    try:
        DotaService(DotaRepository()).get_player_stats(639740, 'L')
        assert False
    except Exception as e:
        assert True


def test_player_stats_by_side():
    try:
        DotaService(DotaRepository()).get_player_stats_by_side(639740, 1)
        assert True
    except Exception as e:
        assert False


def test_player_stats_by_side_bad_user_id():
    try:
        DotaService(DotaRepository()).get_player_stats_by_side(0, 1)
        assert False
    except Exception as e:
        assert True


def test_player_stats_by_side_bad_user_id_letter():
    try:
        DotaService(DotaRepository()).get_player_stats_by_side('L', 1)
        assert False
    except Exception as e:
        assert True


def test_player_stats_by_side_bad_num_matches_letter():
    try:
        DotaService(DotaRepository()).get_player_stats_by_side(639740, 'L')
        assert False
    except Exception as e:
        assert True
