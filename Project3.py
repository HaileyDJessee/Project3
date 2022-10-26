import requests
import pygal
from lxml import html
import json

ChartChoice = 0
ChartType = ["bar_chart", "line_chart"]
DateChoice = ""
Date = '&date=' + DateChoice
Function = ['function=TIME_SERIES_DAILY','function=TIME_SERIES_WEEKLY','function=TIME_SERIES_MONTHLY','function=TIME_SERIES_INTRADAY']
StockData = "y"
StockSymbol = ""
Symbol = ""
TimeSeries = 0

def StockFunc():
    global ChartChoice
    global ChartType
    global Symbol
    global StockData
    global TimeSeries

    print("Stock Data Visualizer")
    print("-----------------------")
    while StockData != "n":
            StockSymbol = input("Enter the stock symbol you are looking for: ")
            if StockSymbol == "":
                print("Error Data Type Invalid")
            else:
                Symbol = '&symbol='+ StockSymbol
                print("Your Symbol was" + Symbol)
                while ChartChoice != 1 and ChartChoice != 2:
                    try:
                        print("Chart Types")
                        print("-----------------------")
                        print("1. Bar")
                        print("2. Line")
                        ChartChoice = int(input("Enter the chart type you want (1, 2): "))
                        if ChartChoice == 1 or ChartChoice == 2: 
                            print("Chart Type selected was " + ChartType[ChartChoice-1])
                    except:
                        print("Chart Types")
                        print("-----------------------")
                        print("1. Bar")
                        print("2. Line")
                        print("Data Error Please Select Either '1' or '2': ")
            while TimeSeries != 1 and TimeSeries != 2 and TimeSeries != 3 and TimeSeries != 4:
                try:
                    print("Select the Time Series of the chart you want to Generate")
                    print("-----------------------")
                    print("1. Daily")
                    print("2. Weekly")
                    print("3. Monthly")
                    print("4. Intraday")     
                    TimeSeries = int(input("Enter time series option (1, 2, 3, 4): "))
                    if TimeSeries == 1:
                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                        print(URL)
                        r = requests.get(URL)
                        data = r.json()
                        print(data)
                        
                    elif TimeSeries == 2:
                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                        print(URL)
                        r = requests.get(URL)
                        data = r.json()
                        print(data)
                    
                    elif TimeSeries == 3:
                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&interval=30min'+ Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                        print(URL)
                        r = requests.get(URL)
                        data = r.json()
                        print(data)
                        
                    elif TimeSeries == 4:
                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&interval=30min'+ Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                        print(URL)
                        r = requests.get(URL)
                        data = r.json()
                        print(data)
                except:
                    print("Select the Time Series of the chart you want to Generate")
                    print("-----------------------")
                    print("1. Daily")
                    print("2. Weekly")
                    print("3. Monthly")
                    print("4. Intraday") 
                    print("Data Error Please Select Either '1','2','3', or '4': ")

            StockData = input("Would you like to view more stock data? Press 'y' to continue or 'n' to exit: ")
            if StockData !="y" and StockData !="n":
                print("Error Data Type Invalid. Please enter 'y' or 'n': ")
                StockData = input("Would you like to view more stock data? Press 'y' to continue or 'n' to exit: ")
            ChartChoice = 0
            StockSymbol = ""
            Symbol = ""
            TimeSeries = 0
StockFunc()
