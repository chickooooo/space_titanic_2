# Spaceship Titanic Competition
<br>
<b>Goal:</b> Predict which passengers are transported to an alternate dimension<br>
<br>
<br>

![spaceship titanic](https://live.staticflickr.com/2258/2502603301_57c6af2a9a_z.jpg "spaceship titanic")
<br>
<br>
<b>Description:</b><br>
The Spaceship Titanic was an interstellar passenger liner launched in 2912. With almost 13,000 passengers on board, the vessel set out on its maiden voyage transporting emigrants from our solar system to three newly habitable exoplanets orbiting nearby stars.<br>
<br>
While rounding Alpha Centauri en route to its first destination—the torrid 55 Cancri E—the unwary Spaceship Titanic collided with a spacetime anomaly hidden within a dust cloud. Sadly, it met a similar fate as its namesake from 1000 years before. Though the ship stayed intact, almost half of the passengers were transported to an alternate dimension!<br>
<br>
To help rescue crews and retrieve the lost passengers, you are challenged to predict which passengers were transported by the anomaly using records recovered from the spaceship’s damaged computer system.<br>
<br>
<b>Evaluation metrics:</b> Accuracy
<br>
<br>
<br>
## Version 1:<br>
[v1](/v1) directory contains base model to set a baseline for model performance.<br>
This directory has pipeline scripts and testcases for those pipelines. Generic testcases to verify the structure of the dataset is also present.<br>
This directory focus more on creating a structure that will ease model development process, rather than focusing on accuracy of the model (refer to v2).<br>
<br>
<br>
## Version 2:<br>
[v2](/v2) directory focus on creating the best performing model.<br>
It contains detailed Exploratory Data Analysis of the data and systematic Missing value imputation.<br>
It also focus on feature engineering and data preprocessing techniques.<br>
At last, selects the best performing model from a variety of models and generates final score.<br>