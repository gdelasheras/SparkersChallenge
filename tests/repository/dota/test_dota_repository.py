from http import HTTPStatus

from stats_app.repository.dota.dota_repository import call_dota_api, DotaRepository


def test_dota_api_call():
    response = call_dota_api(f"https://api.opendota.com/api/matches/6856178688")
    assert response.status_code == HTTPStatus.OK


def test_dota_api_empty_url():
    try:
        response = call_dota_api(None)
        assert False
    except Exception as e:
        assert True
        assert "Error while calling Dota API" in str(e)


def test_dota_api_bad_url():
    try:
        response = call_dota_api("https://api.opendota.com/api/matches/")
        assert False
    except Exception as e:
        assert True


def test_get_matches_data():
    assert DotaRepository().get_matches(639740, 1) is not None


def test_get_matches_data_empty():
    assert DotaRepository().get_matches(0, 1) is None


def test_get_matches_data_bad_id():
    try:
        DotaRepository().get_matches("TEST", 1)
        assert False
    except Exception as e:
        assert True


def test_get_match_data():
    assert DotaRepository().get_match_data(6856178688) is not None


def test_get_match_data_empty():
    try:
        DotaRepository().get_match_data(None)
        assert False
    except Exception as e:
        assert True


def test_get_match_data_bad_id():
    try:
        DotaRepository().get_match_data("TEST")
        assert False
    except Exception as e:
        assert True
