# Relative-Beta
Relative Beta Analysis
IMPORTANT: Must have an Alpha Vantage API Key. They are free at https://www.alphavantage.co/

The goal of this project is to assign a "relative beta" to a list of input companies as a way of measuring what their respective risk is against eachother.

The equation for calculating the "beta" stands as the covariance of the mean values of all companies intramonth percentage changes and each of the companies 
respective intramonth percentage changes divided by the variance of the means.

A.K.A.
cov(m, s)/var(m)

Where:
m = mean
s = stock intramonth percentage changes

The program also charts the intramonth percentage changes of each stock over 5 years (the length of time measured).

Pictured Below is a use case of 5 stocks in the e-commerce business:
AMZN
CHWY
EBAY
ETSY
WMT

![matplot](https://user-images.githubusercontent.com/86123149/136323871-bade6b0e-bf0e-4900-88f2-833807be2cfd.png)
<img width="530" alt="Screen Shot 2021-10-07 at 1 06 54 AM" src="https://user-images.githubusercontent.com/86123149/136323944-ba4c9242-b8c8-45cc-8f3a-84f9ae750414.png">
