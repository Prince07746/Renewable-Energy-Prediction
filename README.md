# AI-Powered-Yelp-Rating-Predictor
This project provides valuable insights into the factors contributing to high Yelp ratings, helping restaurant owners understand what to focus on to improve their establishment's reputation and attract more customers.



# AI-Powered Yelp Rating Predictor

## Project Description

In the competitive restaurant industry, a restaurant's success is often linked to its reputation, which is reflected in its Yelp ratings. This project aims to identify and analyze the factors that most significantly impact a restaurant's Yelp rating using a real dataset provided by Yelp. The dataset includes various features such as business attributes, user reviews, check-ins, and tips.

### The project involves:
1. Cleaning and preparing the data.
2. Analyzing the features.
3. Training a multiple linear regression model.
4. Evaluating the model's performance.
5. Predicting a hypothetical restaurant's Yelp rating based on user-defined features.

This project provides valuable insights into the factors contributing to high Yelp ratings, helping restaurant owners understand what to focus on to improve their establishment's reputation and attract more customers.

## Overview of the Project

### Introduction
The restaurant industry is challenging, with online reviews playing a critical role in a restaurant's success. This project uses Yelp data to investigate which factors most affect a restaurant's rating.

### Dataset
Six JSON files from Yelp:
- `yelp_business.json`: Business attributes and locations.
- `yelp_review.json`: Review metadata by business.
- `yelp_user.json`: User profile metadata.
- `yelp_checkin.json`: Check-in metadata.
- `yelp_tip.json`: Tips metadata.
- `yelp_photo.json`: Photo metadata.

### Data Preparation
- Clean and prepare the data for analysis.
- Analyze the features to understand their distribution and relationships.

### Model Training
- Train a multiple linear regression model to predict Yelp ratings based on the features.

### Model Evaluation
- Evaluate the model's performance using metrics like R² and Mean Absolute Error (MAE).

### Prediction
- Predict the Yelp rating for a hypothetical new restaurant, "Danielle's Delicious Delicacies," based on selected feature values.

## Key Features and Their Statistics

| Feature                     | Mean       | Min        | Max         |
|-----------------------------|------------|------------|-------------|
| alcohol?                    | 0.14       | 0.00       | 1.00        |
| has_bike_parking            | 0.35       | 0.00       | 1.00        |
| takes_credit_cards          | 0.70       | 0.00       | 1.00        |
| good_for_kids               | 0.28       | 0.00       | 1.00        |
| take_reservations           | 0.11       | 0.00       | 1.00        |
| has_wifi                    | 0.13       | 0.00       | 1.00        |
| review_count                | 31.80      | 3.00       | 7968.00     |
| price_range                 | 1.04       | 0.00       | 4.00        |
| average_caption_length      | 2.83       | 0.00       | 140.00      |
| number_pics                 | 1.49       | 0.00       | 1150.00     |
| average_review_age          | 1175.50    | 71.56      | 4727.33     |
| average_review_length       | 596.46     | 62.40      | 4229.00     |
| average_review_sentiment    | 0.55       | -0.99      | 0.99        |
| number_funny_votes          | 15.62      | 0.00       | 36822.00    |
| number_cool_votes           | 18.50      | 0.00       | 6572.00     |
| number_useful_votes         | 43.52      | 0.00       | 38357.00    |
| average_tip_length          | 45.64      | 0.00       | 500.00      |
| number_tips                 | 6.29       | 0.00       | 3581.00     |
| average_number_friends      | 105.13     | 1.00       | 4219.00     |
| average_days_on_yelp        | 2005.37    | 76.00      | 4860.00     |
| average_number_fans         | 11.59      | 0.00       | 1174.67     |
| average_review_count        | 122.11     | 0.67       | 6335.00     |
| average_number_years_elite  | 0.92       | 0.00       | 10.67       |
| weekday_checkins            | 45.39      | 0.00       | 73830.00    |
| weekend_checkins            | 49.61      | 0.00       | 64647.00    |


to find execute
danielles_delicious_delicacies = np.array([0,1,1,1,1,1,10,2,3,10,10,1200,0.9,3,6,5,50,3,50,1800,12,123,0.5,0,0]).reshape(1,-1)
model.predict(danielles_delicious_delicacies)
