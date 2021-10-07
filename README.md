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
