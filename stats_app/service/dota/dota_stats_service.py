from stats_app.repository.dota.dota_repository import DotaRepository
from .stats_calculation.kill_participation import get_player_kill_participation
from .stats_calculation.kills_deaths_assists import get_player_max_min_avg_kda
from ...utils.dota.dota_utils import TEAM_RADIANT, TEAM_DIRE


class DotaService:
    def __init__(self, dota_repository: DotaRepository):
        self.dota_repository = dota_repository

    def get_player_stats(self, player_id, num_games) -> dict:
        """
        Service that retrieves the last 'num_games' games played by 'player_id' and computes the maximum, the minimum
        and the average kda and kill participation.

        :param player_id: Steam id of the player.
        :param num_games: Number of games to retrieve.
        :return: Dictionary with the mentioned data.
        """
        df_matches = self.dota_repository.get_matches(player_id, num_games)

        # Compute stats.
        max_kda, min_kda, mean_kda = get_player_max_min_avg_kda(df_matches.copy())
        max_kp, min_kp, mean_kp = get_player_kill_participation(df_matches.copy())

        return {
            "game": "Dota",
            "player_name": "YrikGood",
            "total_games": df_matches.match_id.nunique(),
            "max_kda": round(max_kda, 2),
            "min_kda": round(min_kda, 2),
            "avg_kda": round(mean_kda, 2),
            "max_kp": str(round(max_kp, 2)) + "%",
            "min_kp": str(round(min_kp, 2)) + "%",
            "avg_kp": str(round(mean_kp, 2)) + "%"
        }

    def get_player_stats_by_side(self, player_id, num_games) -> dict:
        """
        Service that retrieves the last 'num_games' games played by 'player_id' and computes the maximum, the minimum
        and the average kda and kill participation for each team side.

        :param player_id: Steam id of the player.
        :param num_games: Number of games to retrieve.
        :return: Dictionary with the mentioned data.
        """
        df = self.dota_repository.get_matches(player_id, num_games)

        # Filtering by team side.
        df_radiant, df_dire = df[df['side'] == TEAM_RADIANT], df[df['side'] == TEAM_DIRE]

        # Compute Radiant stats.
        radiant_max_kda, radiant_min_kda, radiant_mean_kda = get_player_max_min_avg_kda(df_radiant.copy())
        radiant_max_kp, radiant_min_kp, radiant_mean_kp = get_player_kill_participation(df_radiant.copy())

        # Compute Dire stats.
        dire_max_kda, dire_min_kda, dire_mean_kda = get_player_max_min_avg_kda(df_dire.copy())
        dire_max_kp, dire_min_kp, dire_mean_kp = get_player_kill_participation(df_dire.copy())

        return {
            "game": "Dota",
            "player_name": "YrikGood",
            "total_games": df.match_id.nunique(),
            "radiant_stats":
            {
                "max_kda": round(radiant_max_kda, 2),
                "min_kda": round(radiant_min_kda, 2),
                "avg_kda": round(radiant_mean_kda, 2),
                "max_kp": str(round(radiant_max_kp, 2)) + "%",
                "min_kp": str(round(radiant_min_kp, 2)) + "%",
                "avg_kp": str(round(radiant_mean_kp, 2)) + "%"
            },
            "dire_stats":
            {
                "max_kda": round(dire_max_kda, 2),
                "min_kda": round(dire_min_kda, 2),
                "avg_kda": round(dire_mean_kda, 2),
                "max_kp": str(round(dire_max_kp, 2)) + "%",
                "min_kp": str(round(dire_min_kp, 2)) + "%",
                "avg_kp": str(round(dire_mean_kp, 2)) + "%"
            }
        }
