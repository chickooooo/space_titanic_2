## Creating best performing model
<br>
<br>

### Folder structure:<br>

-- **data**<br>
&nbsp; &nbsp; &nbsp; raw data:<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -- [train](./data/train.csv)<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -- [test](./data/test.csv)<br>
&nbsp; &nbsp; &nbsp; data after imputing misssing values:<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -- [train_2](./data/train_2.csv)<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -- [test_2](./data/test_2.csv)<br>
&nbsp; &nbsp; &nbsp; data after feature engineering:<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -- [train_engineered](./data/train_engineered.csv)<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -- [test_engineered](./data/test_engineered.csv)<br>
&nbsp; &nbsp; &nbsp; data after preprocessing:<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -- [x_train_preprocessed](./data/x_train_preprocessed.csv)<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -- [x_test_preprocessed](./data/x_test_preprocessed.csv)<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -- [y_train_preprocessed](./data/y_train_preprocessed.csv)<br>
&nbsp; &nbsp; &nbsp; submission data:<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -- [submission_1](./data/submission_1.csv)<br>

-- **notebooks**<br>
&nbsp; &nbsp; &nbsp; Exploratory Data Analysis: [eda](./notebooks/eda.ipynb)<br>
&nbsp; &nbsp; &nbsp; Handling Missing Values: [handling_missing_values](./notebooks/handling_missing_values.ipynb)<br>
&nbsp; &nbsp; &nbsp; Feature Engineering: [feature_engineering](./notebooks/feature_engineering.ipynb)<br>
&nbsp; &nbsp; &nbsp; Data Preprocessing: [data_preprocessing](./notebooks/data_preprocessing.ipynb)<br>
&nbsp; &nbsp; &nbsp; Model Selection: [model_selection](./notebooks/model_selection.ipynb)<br>
<br>
<br>
<br>
### Exploratory Data Analysis
Exploratory Data Analysis notebooks contains detailed analysis of the given data and highlights some key findings that are crutial for next steps in the process.<br>
Each section contains a **note** which highlights the important point and **action** which indicates the action that needs to be performed.<br>
<br>
### Handling Missing Values
In Handling Missing Values notebook, instead of just imputing missing values with mode or median, a more systematic approach is used. <br>
Using data from EDA and by looking at relations between 2 or more features, proper imputation of missing value is carried out.<br>
This process was one of the key factor that helped in achieving higher score.<br>
<br>
### Feature Engineering
Some columns have more than 1 features combined together while some columns where not having meaningful data. Also existing features are not fully able to explain the data.<br>
Hence in Feature Engineering notebook, features are extracted, processed and new meaningful features are created.<br>
<br>
### Data Preprocessing
Data preprocessing notebook deals with preprocessing the data, so it is ready to be feed to the model. This includes handling categorical data and text data, scaling numerical data, dealing with outliers, etc.<br>
<br>
### Model Selection
At last, Model Selection notebook scans through a variety of models and selects the best performing model for our usecase.<br>
Once model is selected, it generate predictions and creates a submission file.
<br>
<br>
<br>
<br>
## Conclusion
Final score after submitting the predictions to the competition is 80.5%.<br>
<br>
Rank: **499** /2660<br>
[Spaceship Titanic](https://www.kaggle.com/chickooo/competitions?tab=active)<br>
<br>
Achievements:
- under 500
- top 20%