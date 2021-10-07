import requests
import numpy as np
import constants
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import datetime

# Returns five years prior, useful for filtering Alpha Vantage return content
def get_five_years():
    d = datetime.date.today() - datetime.timedelta(days=5 * 365)
    return str(d)

# This function returns the percentage change month over month
def get_difference(tik):
    ts = TimeSeries(key=constants.av_ak, output_format='pandas')
    data, meta_data = ts.get_monthly_adjusted(symbol=tik)
    data_date_changed = data.sort_index().loc[get_five_years(): str(datetime.date.today())]

    difference = []


    for i in range(1, len(data_date_changed['5. adjusted close'])):
        difference.append(((data_date_changed['5. adjusted close'][i]-data_date_changed['5. adjusted close'][i-1])/
                           data_date_changed['5. adjusted close'][i-1])*100)

    difference.append(sum(difference)/len(difference))
    data_date_changed['relative beta ' + tik] = difference


    return data_date_changed['relative beta ' + tik]


def find_beta(tickers):
    differences = []
    for i in tickers:
        differences.append(get_difference(i))

    data_all = pd.concat(differences, axis=1)
    data_all['mean'] = data_all.mean(axis=1)

    beta_grid = data_all.cov() / data_all['mean'].var()
    print(beta_grid['mean'])

    data_all.plot()
    plt.legend(labels=tickers)
    plt.axhline(y=0, color='b', linestyle='-')
    plt.title('Intramonth Percent Change of Outlined Stocks: ' + str(tickers))
    plt.show()




