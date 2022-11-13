from typing import List

from pandas import DataFrame
from pydantic import BaseModel, Field, ValidationError


class DotaDataFrameRowValidator(BaseModel):
    match_id: int = Field(gt=0)
    kills: int = Field(ge=0)
    deaths: int = Field(ge=0)
    assists: int = Field(ge=0)
    side: int = Field(ge=0, le=1)
    player: bool


class DotaDataFrameValidator(BaseModel):
    df: List[DotaDataFrameRowValidator]


def validate_dota_dataframe(df: DataFrame):
    """
    Validates the dota dataframe, otherwise it throws an exception.
    :param df: Dataframe to validate.
    """
    try:
        DotaDataFrameValidator(df=df.to_dict(orient="records"))
    except ValidationError as e:
        raise Exception("Invalid dataframe format")
