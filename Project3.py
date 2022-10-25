import requests
import pygal
import lxml
StockSymbol =""
TimeSeries = 0
Function = ['function=TIME_SERIES_DAILY','function=TIME_SERIES_WEEKLY','function=TIME_SERIES_MONTHLY','function=TIME_SERIES_INTRADAY']
Date = '&date=2022-06-09'
def StockMod():
    StockData = "y"
    print("Stock Data Visualizer")
    print("-----------------------")
    while StockData != "n":
        if StockData !="y" and StockData !="n":
            print("Error Data Type Invalid. Please enter 'y' or 'n'")
        else:
            try: 
                StockSymbol = input("Enter the stock symbol you are looking for: ")
                if StockSymbol == "":
                    print("Error Data Type Invalid")
                else:
                    Symbol = '&symbol='+ StockSymbol
                    print("Chart Types")
                    print("-----------------------")
                    print("1. Bar")
                    print("2. Line")
                    ChartType = int(input("Enter the chart type you want (1, 2):"))
                    if ChartType == 1:
                        print("you have chosen Bar Chart")
                        print("Select the Time Series of the chart you want to Generate")
                        print("-----------------------")
                        print("1. Daily")
                        print("2. Weekly")
                        print("3. Monthly")
                        print("4. Intraday")
                        TimeSeries = int(input("Enter time series option (1, 2, 3, 4):"))
                        if TimeSeries != 1 and TimeSeries != 2 and TimeSeries != 3 and TimeSeries != 4:
                            print("Error Data Type Invalid")
                        else:
                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&date=2022-06-09'+ Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                            print(URL)
                            StartDate = input("Enter the start date (YYYY-MM-DD):")
                            EndDate = input("Enter the end date (YYYY-MM-DD):")
                            r = requests.get(URL)
                            data = r.json()
                            print(data)
                            #bar_chart = pygal.Bar
                            #bar_chart.add(str(data))
                            #bar_chart.render_in_browser()
                    elif ChartType == 2:
                        print("you have chosen Line Chart")
                        print("Select the Time Series of the chart you want to Generate")
                        print("-----------------------")
                        print("1. Daily")
                        print("2. Weekly")
                        print("3. Monthly")
                        print("4. Intraday")
                        TimeSeries = int(input("Enter time series option (1, 2, 3, 4):"))
                        if TimeSeries != 1 and TimeSeries != 2 and TimeSeries != 3 and TimeSeries != 4:
                            print("Error Data Type Invalid")
                        else:
                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&date=2022-06-09'+ Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                            print(URL)
                            StartDate = input("Enter the start date (YYYY-MM-DD):")
                            EndDate = input("Enter the end date (YYYY-MM-DD):")
                            r = requests.get(URL)
                            data = r.json()
                            print(data)
                            #line_chart = pygal.Line
                            #line_chart.add(str(data))
                            #line_chart.render_in_browser()
                    else:
                        print("Error Data Type Invalid")        
                        StockData = input("Would you like to view more stock data? Press 'y' to continue or 'n' to exit: ")
            except:
                print("Error Data Type Invalid")    
StockMod()
