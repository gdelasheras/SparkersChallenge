TEAM_RADIANT = 1
TEAM_DIRE = 0

RADIANT_POSITIONS = (0, 1, 2, 3, 4)
DIRE_POSITIONS = (128, 129, 130, 131, 132)


def get_team_side(player_slot: int) -> int:
    """
    Returns the team side based on the player_slot.

    :param player_slot: Dota API, player_slot.
    :return: Team side.
    """
    if player_slot in RADIANT_POSITIONS:
        return TEAM_RADIANT
    elif player_slot in DIRE_POSITIONS:
        return TEAM_DIRE
    else:
        raise Exception("Invalid player_slot")
