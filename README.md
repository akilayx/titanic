## Titanic Survival Prediction

My name is Akilay, I am a 10th-grade student, and I am starting to learn data analysis and machine learning. This project is my first practical assignment in this field. It covers the entire data workflow, from exploration and preprocessing to model building and interpretation of results.

The goal of the project is to develop a model that predicts the probability of passenger survival on the Titanic based on available features. The project allows me to apply data processing, analysis, and modeling skills in practice and helps understand which factors influenced passengers’ chances of survival..

*Historical Context*
*The "Titanic" was the largest passenger liner of its time, which sank on April 15, 1912, during its maiden voyage after hitting an iceberg. Over 1,500 people died, despite the ship being considered "unsinkable." This tragedy became a turning point in maritime safety regulations, influencing ship construction and evacuation procedures. The wreck of the Titanic was discovered on the Atlantic Ocean floor in 1985.*
 
![Исторический Титаник](https://litvinovs.net/images/reflection/titanic_shipwreck_versions/titanic.jpg)


## Project Goal
The main objective of this project is to demonstrate understanding of the data workflow and basic machine learning skills, including:

Exploring and analyzing the structure of data

Handling missing values and anomalies

Encoding categorical features and creating new informative features (feature engineering)

Building and comparing multiple machine learning models

Evaluating model performance and interpreting results

Applying theoretical knowledge to practice and visualizing how different factors affect survival chances


## Dataset

The analysis uses the official Titanic datasets from Kaggle:

**train.csv** — contains passenger information and known survival outcomes (Survived)

**test.csv** — contains similar data without the target variable, used for testing the model

Key features used in the project:

**Sex** — passenger gender

**Age** — passenger age

**Pclass** — ticket class / socio-economic status

**SibSp / Parch** — family members on board

**Embarked** — port of embarkation



## Project Workflow

The project follows a step-by-step workflow:

### 1. Data Collection and Preparation

Import data from CSV files (train.csv, test.csv)

Check data structure, feature types, and missing values

Clean data and fill missing values for features like Age and Embarked

Merge and save intermediate tables for further analysis

### 2. Data Preprocessing

Encode categorical variables (Sex, Embarked) into numerical format

Create new features such as:

Total family size (SibSp + Parch + 1)

Adult/Child indicator based on age

Scale and normalize features for machine learning algorithms

### 3. Exploratory Data Analysis (EDA)

Visualize distributions of features (histograms, boxplots, countplots)

Explore the relationship between survival and features like sex, age, ticket class, family size, and port of embarkation

Identify anomalies and potentially important patterns

Check correlations between features and the target variable

### 4. Model Building and Training

Split data into training and testing sets

Train multiple machine learning models:

Logistic Regression

Decision Tree

Random Forest

k-Nearest Neighbors (kNN)

Naive Bayes

Support Vector Classifier (SVC)

Tune hyperparameters and optimize models

Compare models using evaluation metrics

### 5. Model Evaluation

Calculate accuracy, precision, recall, and ROC-AUC

Build a confusion matrix

Identify the model with the best performance and stability

### 6. Results Interpretation

Determine key factors affecting passenger survival:

Gender (women survived more often)

Social class (1st-class passengers had higher survival rates)

Age and family composition on board

Draw conclusions about how these features influence survival chances

## Libraries Used

pandas — data manipulation and analysis

numpy — numerical operations

matplotlib — basic visualizations

seaborn — advanced visualizations

scikit-learn — machine learning models

Jupyter Notebook — interactive analysis and reporting

## Sources and References

(Kaggle Titanic Dataset)[https://www.kaggle.com/competitions/titanic]  
(Pandas Documentation)[https://pandas.pydata.org/docs/]
(Matplotlib Documentation)[https://matplotlib.org/stable/contents.html]
(Seaborn Documentation)[https://seaborn.pydata.org/documentation.html]  
(Scikit-learn Documentation)[https://scikit-learn.org/stable/documentation.html]  
(Kaggle tutorials and blogs on Titanic EDA and machine learning)[https://www.kaggle.com/search?q=titanic+eda]  
(Educational articles on feature engineering and data preprocessing)[https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114]

## Project Outcomes

This project demonstrates the practical application of data analysis and machine learning to a real-world problem: predicting passenger survival. It provides hands-on experience in data cleaning, visualization, feature engineering, modeling, and interpretation of results.
