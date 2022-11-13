import math

import numpy as np
import pandas as pd
from pandas import DataFrame

from stats_app.validators.dota_dataframe_validator import validate_dota_dataframe


def get_player_kill_participation(df_matches: DataFrame) -> tuple:
    """
    Computes the Kill participation ratio per player in each match.
    KP = player kills + player assists / Team kills

    :param df_matches: Dataframe columns: {'match_id', 'kills', 'deaths', 'assists', 'side', 'player'}
    :return: A dataframe with a new column called 'kd'.
    """
    validate_dota_dataframe(df_matches)

    # Grouping teammates on one side and the player on the other side.
    df_matches = df_matches.groupby(['match_id', 'side', 'player']) \
        .agg(total_kills=('kills', np.sum),
             total_assists=('assists', np.sum)) \
        .reset_index(drop=False)

    # Merging both stats in the same row.
    df_player = df_matches[df_matches['player'] == True]
    df_teammates = df_matches[df_matches['player'] != True]
    df_merged = pd.merge(df_player, df_teammates, on=['match_id', 'side'], how='left',
                         suffixes=('_player', '_team_mates'))

    # Computing kill participation.
    df_merged['kp'] = ((df_merged['total_kills_player'] + df_merged['total_assists_player'])
                       / (df_merged['total_kills_team_mates'] + df_merged['total_kills_player'])) * 100

    kp_max = df_merged.kp.max()
    kp_min = df_merged.kp.min()
    kp_avg = df_merged.kp.mean()

    return 0 if math.isnan(kp_max) else round(kp_max, 2), \
           0 if math.isnan(kp_min) else round(kp_min, 2), \
           0 if math.isnan(kp_avg) else round(kp_avg, 2)
