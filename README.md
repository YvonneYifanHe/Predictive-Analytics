# Predictive-Analytics

This project aims to develop a predict model and a decision support system (DSS) that evaluates the risk of Home Equity Line of Credit (HELOC) applications. 


## Dataset Introduction
The dataset and the description of the data could be found by the following link:
https://community.fico.com/s/explainable-machine-learning-challenge

The data set we used for this project is an anonymous data set from a HELOC app created by real homeowners. HELOC is a line of credit that is usually provided by banks. Customers in this data set requested credit lines between $5,000 and $150,000. This model uses information from applicants' credit reports to predict whether they will repay their HELOC account within 2 years. That forecast is then used to determine whether a homeowner qualifies for a line of credit. In this data set, the predicted target variable is a binary variable named “RiskPerformance”. A "bad" value means a consumer is at least 90 days overdue or worse within 24 months of opening a credit account. A value of "good" means they have paid and are not more than 90 days overdue.This dataset consists of 24 variables, each of which describes the historical activity record information between some applicants and banks, which can help us to depict the user portrait of each applicant and predict the risk performance and credit limit of the applicant.  



## Project Design
### 1. Develop a predictive model to assess credit risk
  * Data preprocessing
  * Modele training and evaluation
    * Linear models
      * Logistic regression
      * Naive Bayes
      * SVC
      * K-Nearest Neighbor
      * Linear discriminant analysis
    * Tree-based models
      * Decision trees
      * Ensemble methods - Random forests
      * Ensemble methods - Boosting
      * Bagging


### 2. Develop a prototype of the interactive interface

After trying the above nine models and calculating the accuracy scores of their respective training set, test set and validation set, we decided to put the model with the highest accuracy score into our interface, which is the boosting model with the best parameter combination.

With the selected model, we created a decision support system to help bank or credit card companies to decide on accepting or rejecting applications. The system is an interactive interface where users can input the information about applications, and prediction outcomes would be shown. 

If the estimated outcome shows that the applicant has bad risk performance, you can see “You should reject the application! Estimated outcome indicates that the applicant was 90 days past due or worse at least once over a period of 24 months from when the credit account was opened” on the screen, or you would see “You should accept the application! Estimated outcome indicates that the applicant made their payments without ever being more than 90 days overdue.”

![](https://github.com/YvonneYifanHe/Predictive-Analytics/blob/6ba719a0872d16254b315dfd7694c7e0ad1bc90a/HELOC_streamlit1.png)

![](https://github.com/YvonneYifanHe/Predictive-Analytics/blob/6ba719a0872d16254b315dfd7694c7e0ad1bc90a/HELOC_streamlit2.png)

