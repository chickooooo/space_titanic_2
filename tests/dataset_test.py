"""
Dataset unit tests

- should contain given columns
- missing value percentage for each feature should be less than 30%
- should not have missing values in given features
- should have numerical datatype for given features

"""

import pandas as pd
import numpy as np

# loading dataset
data = pd.read_csv("./data/train.csv")


def test_should_contain_columns() -> None:
    """should contain given columns
    """
    required_columns = ["PassengerId", "HomePlanet", "CryoSleep", "Cabin", "Destination", "Age",
                        "VIP", "RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck", "Name", "Transported"]

    assert list(data.columns) == required_columns


def test_missing_less_than_30() -> None:
    """missing value percentage for each feature should be less than 30%
    """
    total = len(data)
    values = data.isna().sum()

    for value in values:
        assert (value / total) < 0.3


def test_non_null_features() -> None:
    """should not have missing values in given features
    """
    features = ["PassengerId", "Transported"]

    for feature in features:
        assert data[feature].isna().sum() == 0


def test_numerical_features() -> None:
    """should have numerical datatype for given features
    """
    features = ["Age", "RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck"]

    for feature in features:
        assert data[feature].dtype in (np.dtype('float'), np.dtype('int'))