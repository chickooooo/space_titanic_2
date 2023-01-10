import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import RobustScaler

class CustomDataPreprocessing(BaseEstimator, TransformerMixin):

    categorical_attributes = ["home_planet", "destination", "deck", "side", "age_category"]
    boolean_attributes = ["cryo_sleep", "vip"]
    num_attributes = ["age", "room_service", "food_court", "shopping_mall", "spa", "vr_deck", "group", "number_in_group", "num_in_cabin", "total_spending"]

    def __init__(self) -> None:
        self.scaler = RobustScaler()

    def fit(self, X: pd.DataFrame):
        self.scaler.fit(X[self.num_attributes])
        return self
    
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        cat_data = X[self.categorical_attributes].copy()
        bool_data = X[self.boolean_attributes].copy()
        num_data = X[self.num_attributes].copy()
        num_index = num_data.index

        # cat data
        cat_data_encoded = pd.get_dummies(cat_data)

        # bool data
        bool_data_encoded = pd.DataFrame()
        for attribute in self.boolean_attributes:
            bool_data_encoded[attribute] = bool_data[attribute].apply(lambda x: 1 if x else 0)

        # num data
        num_data_scaled = self.scaler.transform(num_data)
        num_data_scaled = pd.DataFrame(num_data_scaled, columns=self.num_attributes, index=num_index)

        data: pd.DataFrame = pd.concat([num_data_scaled, cat_data_encoded, bool_data_encoded, X.gender], axis=1)

        return data