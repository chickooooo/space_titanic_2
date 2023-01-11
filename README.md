## Machine Learning model for predicting transported passengers of Spaceship Titanic
<br>

Complete problem statement available here: [Kaggle Spaceship Titanic](https://www.kaggle.com/competitions/spaceship-titanic).
<br>
<br>
Folder structure:

-- **data** &nbsp; &nbsp; contains datasets<br>
-- **models** &nbsp; &nbsp; contains trained models (in pickle format)<br>
-- **notebooks** &nbsp; &nbsp; contains jupyter notebooks used for data exploration, preparation, proprocessing, etc.<br>
-- **pipelines** &nbsp; &nbsp; contains data pipelines as python scripts<br>
-- **tests** &nbsp; &nbsp; contains test cases for python scripts<br>
-- **main.py** &nbsp; &nbsp; main prediction script for deployed model<br>
-- **main.ipynb** &nbsp; &nbsp; main prediction script during development<br>

<br>
This project focus more on creating a structure that will ease model development process, rather than focusing on accuracy of the model (although that is important as well).<br>
It contains data pipelines that extracts various stages of model development.<br>

- Data Preparation pipeline
- Data Preprocessing pipeline
- Feature Selection pipeline (yet to add)

This extraction also helps in testing of these stages independently.<br>
The **tests** folder contains *unit tests* for each pipeline as well as dataset. Integration tests to check interaction between 2 or more pipelines can also be added in future.<br>
Current test cases only demonstrates the technique that can be used to test the functionality. They do not have 100% coverage of the code.