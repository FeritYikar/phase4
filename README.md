# Nevada Real Estate Investment Opportunities


Authors: Abass Ibrahim, Ferit Yikar, Hatice K. Erdogan

![ameer-basheer-4xKm7qT_RMM-unsplash](https://user-images.githubusercontent.com/94992749/154766049-05c511b2-9700-4bad-99de-dc6f0b3b8f57.jpg)

As Three Modellers Consulting, we have a long background in Data Science with successful anayses and building machine learning models. 

PLM Real Estate has consulted us with the question:<br/>
What are the top 5 best zip codes for us to invest in?

# Data  

We are using the U.S. housing dataset hosted by Zillow. We were provided with time series data with dates ranging from  April, 1996 to April, 2018.
This dataset has sales price, zip codes, size rank, date of sale, and location information for the entire United States. It includes 51 states with over 14,000 zipcodes. 

Since we did not have enough exogenous variables within the data, we collected additional data on macro and micro economical features that might have external  affects on the housing market. We included average household income, inflation rate, real GDP, CPI and unemployment rate as economical features. Additionally, 
we gathered population, land area and population density data as other factors influencing housing prices.

# Methods

We calculated the 5 year percentage change of property values per satate. The top percentage increases were from the West. The top three states were Colorado, Florida and Nevada, we decided to move forward with Nevada as it had the highest percentage change at 64.7%. 

We built zip-code specific models to best predict future prices, we predicted the prices for the next month which is May 2018 and focused on 5 zip-codes that would return the highest profit in Nevada. We deployed several machine learning models including SARIMA, SARIMAX, Facebook Prophet and Recurrent Neural Networks (RNN). We used the extra exogenous variables we collected in SARIMAX model to make better predictions. 


# RNN Model

Our first model is a recurrent neural network model. We built the model with Short Long Term Memory layer. The model is trained on the 80% of our data for each zipcode in Nevada.
When predicting a house price our model is using 60 previous prices(5 years). To get our model to use 60 previous prices we created our y_train values to be all the prices in trin data starting from 61st price. Corresponding X_train sets are 60 previous price values. For example our first X_train value is a list of first 60 prices and corresponding y_train value is 61st price, second X_train value is a list of prices from 2nd to 61st and corresponding y_train value is 62nd price. The same applies for our test sets as well. 

Once we ran the model for our first zipcode we saw some great predictions on unseen data. Then we applied the model to all the zipcodes. 

a picture of the chart here

However your model works great on some zipcodes and not so well on others. Models average MAPE was 20% when applied to all zipcodes. We then run more RNN models with more layers and some dropouts. Different models did well on different zipcodes. Then we ran different type of models to see how succesfull they are on different zipcodes.


# Results 

For our final model, we decided to use the best mix of our models which we called the Fusion Model because we got different Mean Absolute Percentage Error (MAPE) scores for each zipcode. The Fusion Model itirates over the models and takes the model that makes predictions with the least errors for every zipcode and makes predicitons based on that. 



The Udemy course below uses RNN to deal witth a Time Series problem, our models were inspired from this course
https://www.udemy.com/course/deeplearning/learn/lecture/6905302?start=30#content

We found the blog entry below very helpful when building our Facebook Prophet Models
https://mkang32.github.io/python/2020/12/15/prophet-intro.html
