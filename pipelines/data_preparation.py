import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class CustomDataPreparation(BaseEstimator, TransformerMixin):
    
    def __init__(self) -> None:
        self.aggregates = {}

    def fit(self, X: pd.DataFrame):
        self.columns = X.columns
        self.__get_aggregates(X)
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        data = pd.DataFrame()

        # filling null values of current column
        for column in self.columns:
            if column not in ["passenger_id", "cabin", "name"]:
                data[column] = X[column].fillna(value=self.aggregates[column])

        # creating new columns
        data["group"] = X.passenger_id.apply(lambda x: int(x.split("_")[0]))
        data["number_in_group"] = X.passenger_id.apply(lambda x: int(x.split("_")[1]))

        data["deck"] = X.cabin.apply(lambda x: x.split("/")[0] if pd.notna(x) else x)
        data["num_in_cabin"] = X.cabin.apply(lambda x: x.split("/")[1] if pd.notna(x) else x)
        data["side"] = X.cabin.apply(lambda x: x.split("/")[2] if pd.notna(x) else x)
        data.deck.fillna(value=self.aggregates["deck"], inplace=True)
        data.side.fillna(value=self.aggregates["side"], inplace=True)
        data.num_in_cabin.fillna(value=self.aggregates["num_in_cabin"], inplace=True)
        data.num_in_cabin = data.num_in_cabin.astype("int")

        data["total_spending"] = data.room_service + data.food_court + data.shopping_mall + data.spa + data.vr_deck

        data["age_category"] = data.age.apply(lambda x: self.__get_age_category(x))

        data["gender"] = X.name.apply(lambda x: self.__get_gender(x))
        data.gender.fillna(value=1.0, inplace=True)

        return data

    def __get_aggregates(self, X: pd.DataFrame) -> None:
        self.aggregates["home_planet"] = X.home_planet.mode()[0]
        self.aggregates["cryo_sleep"] = X.cryo_sleep.mode()[0]

        deck = X.cabin.apply(lambda x: x.split("/")[0] if pd.notna(x) else x)
        side = X.cabin.apply(lambda x: x.split("/")[2] if pd.notna(x) else x)
        self.aggregates["deck"] = deck.mode()[0]
        self.aggregates["num_in_cabin"] = 0
        self.aggregates["side"] = side.mode()[0]

        self.aggregates["destination"] = X.destination.mode()[0]
        self.aggregates["vip"] = X.vip.mode()[0]
        self.aggregates["age"] = X.age.median()

        self.aggregates["room_service"] = 0.0
        self.aggregates["food_court"] = 0.0
        self.aggregates["shopping_mall"] = 0.0
        self.aggregates["spa"] = 0.0
        self.aggregates["vr_deck"] = 0.0

    def __get_age_category(self, age: float) -> str:
        if age <= 16:
            return "child"
        elif age <= 30:
            return "young_adult"
        elif age <= 45:
            return "middle_adult"
        else:
            return "old_adult"

    def __get_gender(self, name: str) -> int:
        if pd.isna(name):
            return np.nan
        if name.split(" ")[0][-1] in ["a", "e", "i", "y"]:
            return 0
        else:
            return 1