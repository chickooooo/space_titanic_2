import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class CustomDataPreparation(BaseEstimator, TransformerMixin):

    column_names = ["passenger_id", "home_planet", "cryo_sleep", "cabin", "destination", "age", "vip", "room_service", "food_court", "shopping_mall", "spa", "vr_deck", "name"]
    
    def __init__(self) -> None:
        self.aggregates = {}

    def fit(self, X: pd.DataFrame):
        self.__get_aggregates(X)
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        data = pd.DataFrame()
        x_copy = X.copy()
        x_copy.columns = self.column_names

        # filling null values of current column
        for column in self.column_names:
            if column not in ["passenger_id", "cabin", "name"]:
                data[column] = x_copy[column].fillna(value=self.aggregates[column])

        # creating new columns
        data["group"] = x_copy.passenger_id.apply(lambda x: int(x.split("_")[0]))
        data["number_in_group"] = x_copy.passenger_id.apply(lambda x: int(x.split("_")[1]))

        data["deck"] = x_copy.cabin.apply(lambda x: x.split("/")[0] if pd.notna(x) else x)
        data["num_in_cabin"] = x_copy.cabin.apply(lambda x: x.split("/")[1] if pd.notna(x) else x)
        data["side"] = x_copy.cabin.apply(lambda x: x.split("/")[2] if pd.notna(x) else x)
        data.deck.fillna(value=self.aggregates["deck"], inplace=True)
        data.side.fillna(value=self.aggregates["side"], inplace=True)
        data.num_in_cabin.fillna(value=self.aggregates["num_in_cabin"], inplace=True)
        data.num_in_cabin = data.num_in_cabin.astype("int")

        data["total_spending"] = data.room_service + data.food_court + data.shopping_mall + data.spa + data.vr_deck

        data["age_category"] = data.age.apply(lambda x: self.__get_age_category(x))

        data["gender"] = x_copy.name.apply(lambda x: self.__get_gender(x))
        data.gender.fillna(value=1.0, inplace=True)

        return data

    def __get_aggregates(self, X: pd.DataFrame) -> None:
        self.aggregates["home_planet"] = X.HomePlanet.mode()[0]
        self.aggregates["cryo_sleep"] = X.CryoSleep.mode()[0]

        deck = X.Cabin.apply(lambda x: x.split("/")[0] if pd.notna(x) else x)
        side = X.Cabin.apply(lambda x: x.split("/")[2] if pd.notna(x) else x)
        self.aggregates["deck"] = deck.mode()[0]
        self.aggregates["num_in_cabin"] = 0
        self.aggregates["side"] = side.mode()[0]

        self.aggregates["destination"] = X.Destination.mode()[0]
        self.aggregates["vip"] = X.VIP.mode()[0]
        self.aggregates["age"] = X.Age.median()

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