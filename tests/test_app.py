from stats_app.app import App
from stats_app.repository.dota.dota_repository import DotaRepository
from stats_app.service.dota.dota_stats_service import DotaService


def test_app_choice_global_stats():
    try:
        App(DotaService(DotaRepository())).process_option(1, 1)
        assert True
    except Exception as e:
        assert False


def test_app_choice_by_side_stats():
    try:
        App(DotaService(DotaRepository())).process_option(2, 1)
        assert True
    except Exception as e:
        assert False


def test_app_bad_choice_letter():
    App(DotaService(DotaRepository())).process_option('d', 1)


def test_app_bad_choice_number():
    App(DotaService(DotaRepository())).process_option(3, 1)


def test_app_bad_num_matches_number():
    App(DotaService(DotaRepository())).process_option(3, 'L')
