from stats_app.app import App
from stats_app.repository.dota.dota_repository import DotaRepository
from stats_app.service.dota.dota_stats_service import DotaService

if __name__ == "__main__":
    App(DotaService(DotaRepository())).run()
