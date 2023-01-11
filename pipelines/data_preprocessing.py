import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import RobustScaler

class CustomDataPreprocessing(BaseEstimator, TransformerMixin):
    """Encodes categorical features, transforms boolean features and scales Numerical features
    """

    # categorical features
    categorical_attributes = ["home_planet", "destination", "deck", "side", "age_category"]
    # boolean features
    boolean_attributes = ["cryo_sleep", "vip"]
    # numerical features
    num_attributes = ["age", "room_service", "food_court", "shopping_mall", "spa", "vr_deck", "group", "number_in_group", "num_in_cabin", "total_spending"]
    # column order of final data
    column_order = ['age', 'room_service', 'food_court', 'shopping_mall', 'spa', 'vr_deck',
       'group', 'number_in_group', 'num_in_cabin', 'total_spending',
       'home_planet_Earth', 'home_planet_Europa', 'home_planet_Mars',
       'destination_55 Cancri e', 'destination_PSO J318.5-22',
       'destination_TRAPPIST-1e', 'deck_A', 'deck_B', 'deck_C', 'deck_D',
       'deck_E', 'deck_F', 'deck_G', 'deck_T', 'side_P', 'side_S',
       'age_category_child', 'age_category_middle_adult',
       'age_category_old_adult', 'age_category_young_adult', 'cryo_sleep',
       'vip', 'gender']

    def __init__(self) -> None:
        # creates scaler object
        self.scaler = RobustScaler()

    def fit(self, X: pd.DataFrame):
        # fits numerical data to scaler ovject
        self.scaler.fit(X[self.num_attributes])
        return self
    
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        # seperating categorical data
        cat_data = X[self.categorical_attributes].copy()
        # seperating boolean data
        bool_data = X[self.boolean_attributes].copy()
        # seperating numerical data
        num_data = X[self.num_attributes].copy()
        num_index = num_data.index

        # encoding cat data
        cat_data_encoded = pd.get_dummies(cat_data)

        # transforming bool data
        bool_data_encoded = pd.DataFrame()
        for attribute in self.boolean_attributes:
            bool_data_encoded[attribute] = bool_data[attribute].apply(lambda x: 1 if x else 0)

        # scaling num data
        num_data_scaled = self.scaler.transform(num_data)
        # converting NDArray to DataFrame
        num_data_scaled = pd.DataFrame(num_data_scaled, columns=self.num_attributes, index=num_index)

        # combining into single dataframe
        data: pd.DataFrame = pd.concat([num_data_scaled, cat_data_encoded, bool_data_encoded, X.gender], axis=1)
        # preserving order of columns
        data = data[self.column_order]

        return data