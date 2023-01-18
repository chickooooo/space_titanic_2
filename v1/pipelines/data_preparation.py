import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class CustomDataPreparation(BaseEstimator, TransformerMixin):
    """Update column names, fill missing values, create new features
    """

    # column names as per naming conventions
    column_names = ["passenger_id", "home_planet", "cryo_sleep", "cabin", "destination", "age", "vip", "room_service", "food_court", "shopping_mall", "spa", "vr_deck", "name"]
    
    def __init__(self) -> None:
        # will hold feature aggregates
        self.aggregates = {}

    def fit(self, X: pd.DataFrame):
        # get feature aggregates
        self.__get_aggregates(X)
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """transforms training or test data into required dataset

        Args:
            X (pd.DataFrame): training or test data

        Returns:
            pd.DataFrame: required dataset
        """

        # required data
        data = pd.DataFrame()

        x_copy = X.copy()
        # updating column names
        x_copy.columns = self.column_names

        # filling null values with aggregates
        for column in self.column_names:
            if column not in ["passenger_id", "cabin", "name"]:
                data[column] = x_copy[column].fillna(value=self.aggregates[column])

        # creating new columns
        data["group"] = x_copy.passenger_id.apply(lambda x: int(x.split("_")[0]))
        data["number_in_group"] = x_copy.passenger_id.apply(lambda x: int(x.split("_")[1]))

        data["deck"] = x_copy.cabin.apply(lambda x: x.split("/")[0] if pd.notna(x) else x)
        data["num_in_cabin"] = x_copy.cabin.apply(lambda x: x.split("/")[1] if pd.notna(x) else x)
        data["side"] = x_copy.cabin.apply(lambda x: x.split("/")[2] if pd.notna(x) else x)
        # filling null values
        data.deck.fillna(value=self.aggregates["deck"], inplace=True)
        data.side.fillna(value=self.aggregates["side"], inplace=True)
        data.num_in_cabin.fillna(value=self.aggregates["num_in_cabin"], inplace=True)
        # changing type from object to int
        data.num_in_cabin = data.num_in_cabin.astype("int")

        # combining spending
        data["total_spending"] = data.room_service + data.food_court + data.shopping_mall + data.spa + data.vr_deck

        # creating age category
        data["age_category"] = data.age.apply(lambda x: self.__get_age_category(x))

        # creating gender feature
        data["gender"] = x_copy.name.apply(lambda x: self.__get_gender(x))
        # filling missing gender with male
        data.gender.fillna(value=1.0, inplace=True)

        return data

    def __get_aggregates(self, X: pd.DataFrame) -> None:
        """saves aggregate value for each feature

        Args:
            X (pd.DataFrame): training dataset
        """

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

        # default value of 0.0
        self.aggregates["room_service"] = 0.0
        self.aggregates["food_court"] = 0.0
        self.aggregates["shopping_mall"] = 0.0
        self.aggregates["spa"] = 0.0
        self.aggregates["vr_deck"] = 0.0

    def __get_age_category(self, age: float) -> str:
        """create age category from age feature

        Args:
            age (float): age of passenger

        Returns:
            str: age category to which the passenger belongs
        """
        if age <= 16:
            return "child"
        elif age <= 30:
            return "young_adult"
        elif age <= 45:
            return "middle_adult"
        else:
            return "old_adult"

    def __get_gender(self, name: str) -> int:
        """identify gender from name feature

        Args:
            name (str): name of passenger

        Returns:
            int: 1 -> male, 0 -> female
        """
        if pd.isna(name):
            return np.nan
        if name.split(" ")[0][-1] in ["a", "e", "i", "y"]:
            return 0
        else:
            return 1