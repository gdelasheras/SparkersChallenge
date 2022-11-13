import math

import numpy as np
from pandas import DataFrame

from stats_app.validators.dota_dataframe_validator import validate_dota_dataframe


def get_kda(df_matches: DataFrame, compute_only_current_player: bool = False) -> DataFrame:
    """
    Computes the KDA ratio (Kills Deaths Assists) per player in each match.
    KDA = K(ills) + A(ssists) / D(eaths)

    :param df_matches: Dataframe columns: {'match_id', 'kills', 'deaths', 'assists', 'side', 'player'}
    :param compute_only_current_player: If True, the function filters the dataframe by 'player' = True.
    :return: A dataframe with a new column called 'kda'.
    """
    validate_dota_dataframe(df_matches)

    if compute_only_current_player:
        df_matches = df_matches[df_matches['player'] == True].reset_index(drop=True)

    # Prevent the zero division error.
    df_matches['deaths'] = np.where(df_matches['deaths'] == 0, 1, df_matches['deaths'])
    df_matches['kda'] = (df_matches['kills'] + df_matches['assists']) / df_matches['deaths']

    return df_matches


def get_player_max_min_avg_kda(df_matches: DataFrame) -> tuple:
    """
    Computes the maximum, the minimum and the average kill participation for a player.

    :param df_matches: Dataframe columns: {'match_id', 'kills', 'deaths', 'assists', 'side', 'player'}
    :return: Maximum, the minimum and the average kda for a player.
    """
    df_matches = get_kda(df_matches, compute_only_current_player=True)

    kda_max = df_matches.kda.max()
    kda_min = df_matches.kda.min()
    kda_avg = df_matches.kda.mean()

    return 0 if math.isnan(kda_max) else round(kda_max, 2), \
           0 if math.isnan(kda_min) else round(kda_min, 2), \
           0 if math.isnan(kda_avg) else round(kda_avg, 2)
