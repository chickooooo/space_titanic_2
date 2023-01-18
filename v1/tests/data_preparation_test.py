"""
Data Preparation unit tests

- init
    -- should create aggregates dict when initialised

- fit
    -- should have given keys in aggregate dict
    -- should have given key value pair in aggregate dict

- transform
    -- output data should have same number of instances as input data
    -- should have given columns in output data
    -- all features of output data should be non null
    -- output data should have columns with given datatype

"""

import pandas as pd
import numpy as np

import os
import sys
sys.path.append(os.getcwd())
from pipelines.data_preparation import CustomDataPreparation


data = pd.read_csv("./data/train.csv")
data = data.iloc[:1000, :]
data.drop(["Transported"], axis=1, inplace=True)


def test_create_aggregate_dict() -> None:
    """should create aggregates dict when initialised
    """
    dp = CustomDataPreparation()

    assert dp.aggregates == {}


def test_aggregate_dict_keys() -> None:
    """should have given keys in aggregate dict
    """
    dp = CustomDataPreparation()
    keys = ["home_planet", "cryo_sleep", "deck", "num_in_cabin", "side", "destination",
            "vip", "age", "room_service", "food_court", "shopping_mall", "spa", "vr_deck"]

    dp.fit(data)
    assert list(dp.aggregates.keys()) == keys


def test_aggregate_key_value_pair() -> None:
    """should have given key value pair in aggregate dict
    """
    dp = CustomDataPreparation()
    key_value = {
        "home_planet": "Earth",
        "cryo_sleep": False,
        "deck": "F",
        "num_in_cabin": 0,
        "side": "S",
        "destination": "TRAPPIST-1e",
        "vip": False,
        "age": 27.0,
        "room_service": 0.0,
        "food_court": 0.0,
        "shopping_mall": 0.0,
        "spa": 0.0,
        "vr_deck": 0.0 
    }

    dp.fit(data)
    assert dp.aggregates == key_value


def test_same_no_of_instances() -> None:
    """output data should have same number of instances as input data
    """
    dp = CustomDataPreparation()
    dp.fit(data)

    result = dp.transform(data)
    assert len(result) == len(data)


def test_output_columns() -> None:
    """should have given columns in output data
    """
    dp = CustomDataPreparation()
    dp.fit(data)
    columns = {"home_planet", "cryo_sleep", "deck", "num_in_cabin", "side", "destination", "vip", "age", "room_service", "food_court", "shopping_mall", "spa", "vr_deck", "group", "number_in_group", "total_spending", "age_category", "gender"}

    result = dp.transform(data)
    assert set(result.columns) == columns


def test_non_null_features() -> None:
    """all features of output data should be non null
    """
    dp = CustomDataPreparation()
    dp.fit(data)

    result = dp.transform(data)

    for column in result.columns:
        assert result[column].isna().sum() == 0


def test_column_datatype() -> None:
    """output data should have columns with given datatype
    """
    dp = CustomDataPreparation()
    dp.fit(data)
    columns = ["num_in_cabin", "age", "room_service", "food_court", "shopping_mall", "spa", "vr_deck", "group", "number_in_group", "total_spending", "gender"]

    result = dp.transform(data)

    for column in columns:
        assert result[column].dtype in (np.dtype('float64'), np.dtype('int64'), np.dtype('int32'))
