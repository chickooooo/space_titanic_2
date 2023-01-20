## Creating base model
<br>
<br>

### Folder structure:

-- **data** &nbsp; &nbsp; contains datasets<br>
-- **models** &nbsp; &nbsp; contains trained models (in pickle format)<br>
-- **notebooks** &nbsp; &nbsp; contains jupyter notebooks used for data exploration, preparation, proprocessing, etc.<br>
-- **pipelines** &nbsp; &nbsp; contains data pipelines as python scripts<br>
-- **tests** &nbsp; &nbsp; contains test cases for python scripts<br>
-- **main.py** &nbsp; &nbsp; main prediction script for deployed model<br>
-- **main.ipynb** &nbsp; &nbsp; main prediction script during development<br>
<br>

### Abstract
This project focus more on creating a structure that will ease model development process, rather than focusing on accuracy of the model. Refer to [v2](../v2) directory for best performing model.<br>
Testing data pipelines and ensuring the structure of data feed to the model is of proper format, is a crutial part of machine learning model development. So, this project also demonstrates how testcases can be created to test different parts of the model building process. Here **pytest** testing framework is used to create testcases.<br>
<br>

This project contains **Data Preparation** and **Data Preprocessing** pipelines and their respective testcases for testing those pipelines.<br>
For a slightly larger project, `pipelines` folder tends to contain following pipelines:
- Imputation
- Feature Engineering
- Feature Selection
- Data Preprocessing
- Model Selection
- Modelling
- Prediction, etc.
<br>
<br>

The `tests` folder contains unit tests for **Data Preparation** pipelines and raw dataset. It demonstrates how unit tests can be written to test any pipeline and dataset structure.<br>
Along with unit tests, automated integration tests can also be written in similar fashion, to test the interaction between 2 or more pipelines <br>

Note: `tests` folder only demonstrates how to test different functionalities and does not offer full coverage (although it is achievable).<br>

At last, `main.py` will contain the prediction script when model is deployed to the production.
