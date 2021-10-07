import alpha

def take_input():
    tickers = []
    val = input("Enter ticker (Enter '' to run regression): ")
    while val != '':
        tickers.append(val)
        val = input("Enter ticker (Enter '' to run regression): ")

    return tickers
if __name__ == '__main__':
    print("Welcome to the Relative Beta Analysis Project.")
    print("Enter as many stock and etf tickers as you'd like to compare.")
    print("The program will calculate each stock's month over month \n"
          "percentage return. It will then create a mean regression \n"
          "taking the average percentage return. Finally, it will calculate \n"
          "a relative Beta using the equation covariance(m, s)/variance(m) \n"
          "where m is the mean and s is a given stock \n"
          "It will also plot each stocks monthly returns and show that plot \n")


    tickers = take_input()
    alpha.find_beta(tickers)
    # alpha.calc_beta()


