import multiprocessing as mp
import time
from http import HTTPStatus
from typing import Optional

import pandas as pd
import requests
from pandas import DataFrame
from requests import Response

from stats_app.utils.dota.dota_utils import get_team_side


def call_dota_api(url: str) -> Response:
    """
    Requests data from an endpoint of the dota API. If exceeds the API rate, it waits 5 seconds and tries again.

    :param url: Endpoint.
    :return: Data returned by the API.
    """
    while True:
        try:
            response = requests.get(url)
        except:
            raise Exception(f"Error while calling Dota API: {url}")
        if response.status_code == HTTPStatus.OK:
            return response
        elif response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
            print(url + " " + response.json()['error'] + ". Waiting 5 seconds.")
            time.sleep(5)
        else:
            raise Exception(response.json()['error'])


class DotaRepository:

    def get_matches(self, player_id: int, num_matches: int) -> DataFrame:
        """
        Gets last 'num_matches' matches from a 'player_id'.
        :param num_matches: Number of matches to retrieve.
        :param player_id: Identifier of the player.
        :return: Dataframe ['match_id', 'player_slot', 'kills', 'deaths', 'assists', 'player'].
        """
        matches = call_dota_api(f"https://api.opendota.com/api/players/{player_id}/matches?limit={num_matches}")
        if matches.text and matches.text != '[]':
            match_ids = [match['match_id'] for match in matches.json()]

            # Parallel calls.
            with mp.Pool(mp.cpu_count()) as pool:
                df = pool.map(self.get_match_data, match_ids)

            df = pd.concat(df, ignore_index=True)
            df['player'] = df['account_id'] == player_id
            del df['account_id']

            return df
        else:
            return None

    def get_match_data(self, match_id) -> Optional[DataFrame]:
        """
        Gets the data from a 'match_id'.
        :param match_id: Match identifier.
        :return: Dataframe ['match_id', 'account_id', 'kills', 'deaths', 'assists', 'side'].
        """
        match_data = call_dota_api(f"https://api.opendota.com/api/matches/{match_id}")

        if match_data.text:
            df = pd.DataFrame(match_data.json()['players'])
            df = df[['match_id', 'player_slot', 'account_id', 'kills', 'deaths', 'assists']]
            df['side'] = df['player_slot'].apply(get_team_side)
            del df['player_slot']
            return df
        else:
            return None
