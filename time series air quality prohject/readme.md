
Title: Air Quality Forecasting using Time Series Machine Learning Models
Objective

The objective of this project assignment is to develop a machine learning model that predicts future air quality levels based on historical air quality data and relevant environmental factors. Students will gain practical experience in time series analysis, feature engineering, model selection, and evaluation for air quality forecasting.

A few years ago, China established the Air Quality Index (AQI) based on the level of five pollutants atmospheres, namely sulfur dioxide (SO2), nitrogen dioxide (NO2), particulate matter (PM10), carbon monoxide (CO) and ozone (O3) measured at the monitoring stations in each city. 

The dataset consists of hourly atmospheric measurements from 12 cities in Beijing, covering the period from March 1st, 2013, to February 28th, 2017. The target variables are PM2.5, PM10, SO2, NO2, CO, and O3, along with independent variables like temperature, pressure, dew point temperature, rainfall, wind speed, and wind direction.
Requirements

    Dataset: You can use the one provided or let your instructor know the alternative you prefer.
    Data Preprocessing:
        Students should handle any missing values, outliers, or erroneous readings in the dataset to ensure data quality.
        Students should consider temporal resolutions (hourly, daily) and choose an appropriate aggregation level for the analysis.
        Students should split the dataset into training and testing sets, ensuring a sufficient time duration for each set.
    Feature Engineering:
        Students should engineer relevant features from the historical air quality data. Examples include lagged variables, moving averages, time-based indicators, and meteorological data like temperature, humidity, wind speed, or atmospheric pressure.
        Students should consider the influence of external factors, such as industrial activities, geographical attributes, or seasonal variations, on air quality.
    Model Selection and Training:
        Students should explore and experiment with various time series machine learning models suitable for air quality forecasting, such as ARIMA, SARIMA, Prophet, or LSTM.
        Students should train multiple models using the training dataset and tune the model hyperparameters, if applicable.
        Students should compare the performance of different models using appropriate evaluation metrics, such as RMSE, MAE, or accuracy measures specific to air quality indices.
    Model Evaluation and Visualization:
        Students should evaluate the performance of the selected model(s) on the testing dataset.
        Students should visualize the predicted air quality levels alongside the actual values to assess the accuracy and reliability of their model.
        Students should analyze and interpret the model’s performance, discussing its ability to capture pollution patterns, handle seasonality, and make accurate forecasts.

Bonus Challenge

            Students can explore advanced topics, such as ensemble methods, hybrid models, or spatial-temporal modeling techniques to incorporate spatial correlations and neighboring air quality stations.
            Students can investigate the impact of additional data sources, such as satellite imagery, land use information, or real-time sensor data, on air quality forecasting.
            Students can develop visualizations or interactive dashboards to communicate the forecasted air quality information effectively.

Remember to document your process, explain your decisions, and present your results effectively. Good luck with your project!
Important Notes

    Any data pre-processing steps must be presented and justified.
    All algorithms and parameters used must be indicated.
    The organization of the text and presentation, clarity of language and ideas are rewarded.
    Long sequences of poorly formatted results are penalized.
    The report should also make reference to any source used and make explicit which part of the work was influenced by her.
    It is important that your code does not depend on an absolute path, so that it can be executed anywhere. computer. This project should be posted in your GitHub repo with the data. You can split your notebooks into 2 or 3 for better readability. 
    If the notebook contains code that takes a long time to run, it should be included with the option eval=FALSE so that the code is not executed. If the output of your code is needed, you can execute it locally on your computer, save it to a binary file, and load it into your report.

 
Your Feedback Matters!

At Zindua School, we are committed to continuously improving your learning experience. Each week, we provide a short feedback form to understand what’s working well and where we can improve.

By sharing your thoughts, you help us refine our content, enhance support, and ensure a better learning experience for both you and future students. The form takes just a minute to complete, and your insights are invaluable in shaping the program.

👉 Please take a moment to fill out this week’s feedback form here: Weekly Feedback Form
