# phase4
Nevada Real Estate Investment Opportunities




RNN Model

Our first model is a recurrent neural network model. We built the model with Short Long Term Memory layer. The model is trained on the 80% of our data for each zipcode in Nevada.
When predicting a house price our model is using 60 previous prices(5 years). To get our model to use 60 previous prices we created our y_train values to be all the prices in trin data starting from 61st price. Corresponding X_train sets are 60 previous price values. For example our first X_train value is a list of first 60 prices and corresponding y_train value is 61st price, second X_train value is a list of prices from 2nd to 61st and corresponding y_train value is 62nd price. The same applies for our test sets as well. 

Once we ran the model for our first zipcode we saw some great predictions on unseen data. Then we applied the model to all the zipcodes. 

a picture of the chart here

However your model works great on some zipcodes and not so well on others. Models average MAPE was 20% when applied to all zipcodes. We then run more RNN models with more layers and some dropouts. Different models did well on different zipcodes. Then we ran different type of models to see how succesfull they are on different zipcodes.








The Udemy course below uses RNN to deal witth a Time Series problem, our models were inspired from this course
https://www.udemy.com/course/deeplearning/learn/lecture/6905302?start=30#content

We found the blog entry below very helpful when building our Facebook Prophet Models
https://mkang32.github.io/python/2020/12/15/prophet-intro.html