import time

from stats_app.service.dota.dota_stats_service import DotaService
from stats_app.validators.menu_validator import validate_digit_menu_option, validate_positive_number

FIRST_MENU = "\n1 - Get player stats\n2 - Get player stats by side\n3 - Exit\n>> "
NUM_GAMES_MENU = "\nSelect number of games to process\n>> "
USER_ID = 639740


class App:
    def __init__(self, dota_service: DotaService):
        self.dota_service = dota_service

    def run(self):
        """
        Application main loop.
        """
        while True:
            try:
                option = validate_digit_menu_option(input(FIRST_MENU), (1, 2, 3))
                if option == 3:
                    break
                num_games = validate_positive_number(input(NUM_GAMES_MENU), 100)
                self.process_option(option, num_games)
            except Exception as e:
                print("Error: ", e)

    def process_option(self, choice: int, num_games: int):
        """
        Process user's option.
        1 - global stats.
        2 - stats per side (radiant/dire).
        3 - exit

        :param choice: User's choice.
        :param num_games: Number of games to retrieve.
        """
        end = False
        start = time.time()
        if choice == 1:
            print(f"\n{self.dota_service.get_player_stats(USER_ID, num_games)}")
        elif choice == 2:
            print(f"\n{self.dota_service.get_player_stats_by_side(USER_ID, num_games)}")
        elif choice == 3:
            end = True
        print(f"In {round(time.time() - start, 2)} seconds")
        return end
