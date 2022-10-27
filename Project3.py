import requests
import pygal
from lxml import html
import json

ChartChoice = 0
ChartType = ["pygal.Bar(fill=True)", "pygal.Line(fill=False)"]
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
                        if ChartChoice == 1:
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
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Time Series (Daily)']
                                        Index = list(StepData).index(input('Please enter Start Date: '))
                                        Index2 = list(StepData).index(input('Please enter End Date: '))
                                        Value = list(StepData.values())[Index]
                                        Value2 = list(StepData.values())[Index2]
                                        Close =[]
                                        Date =[]
                                        High = []
                                        Low =[]
                                        Open =[]
                                        while Index2 < Index:
                                            Index2 = Index2 + 1
                                            Value2 = list(StepData.values())[Index2]
                                            Date.append(str(list(StepData.keys())[Index2]))
                                            Open.append(int(float(Value2.get("1. open"))))
                                            High.append(int(float(Value2.get("2. high"))))
                                            Low.append(int(float(Value2.get("3. low"))))
                                            Close.append(int(float(Value2.get("4. close"))))
                                        Date.reverse()
                                        Open.reverse()
                                        High.reverse()
                                        Low.reverse()
                                        Close.reverse()
                                        print(Open)
                                        print(Close)
                                        print(High)
                                        print(Low)
                                        print(Date)
                                        bar_chart = pygal.Bar(spacing=100, fill=True, x_label_rotation=20)
                                        bar_chart.title = (StockSymbol +' Stock Data')
                                        bar_chart.x_labels =('Red', 'Blue', 'Green', 'Yellow')
                                        bar_chart.x_labels = Date
                                        bar_chart.add('Open', Open)
                                        bar_chart.add('High', Close)
                                        bar_chart.add('Low', Low)
                                        bar_chart.add('close', Close)
                                        bar_chart.render_in_browser()
                                        break

                                    elif TimeSeries == 2:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Weekly Time Series']
                                        Index = list(StepData).index(input('Please enter Start Date: '))
                                        Index2 = list(StepData).index(input('Please enter End Date: '))
                                        Value = list(StepData.values())[Index]
                                        Value2 = list(StepData.values())[Index2]
                                        Close =[]
                                        Date =[]
                                        High = []
                                        Low =[]
                                        Open =[]
                                        while Index2 < Index:
                                            Index2 = Index2 + 1
                                            Value2 = list(StepData.values())[Index2]
                                            Date.append(str(list(StepData.keys())[Index2]))
                                            Open.append(int(float(Value2.get("1. open"))))
                                            High.append(int(float(Value2.get("2. high"))))
                                            Low.append(int(float(Value2.get("3. low"))))
                                            Close.append(int(float(Value2.get("4. close"))))
                                        Date.reverse()
                                        Open.reverse()
                                        High.reverse()
                                        Low.reverse()
                                        Close.reverse()
                                        print(Open)
                                        print(Close)
                                        print(High)
                                        print(Low)
                                        print(Date)
                                        bar_chart = pygal.Bar(spacing=100, fill=True, x_label_rotation=20)
                                        bar_chart.title = (StockSymbol +' Stock Data')
                                        bar_chart.x_labels =('Red', 'Blue', 'Green', 'Yellow')
                                        bar_chart.x_labels = Date
                                        bar_chart.add('Open', Open)
                                        bar_chart.add('High', Close)
                                        bar_chart.add('Low', Low)
                                        bar_chart.add('close', Close)
                                        bar_chart.render_in_browser()
                                        break
                                    
                                    elif TimeSeries == 3:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Monthly Time Series']
                                        Index = list(StepData).index(input('Please enter Start Date: '))
                                        Index2 = list(StepData).index(input('Please enter End Date: '))
                                        Value = list(StepData.values())[Index]
                                        Value2 = list(StepData.values())[Index2]
                                        Close =[]
                                        Date =[]
                                        High = []
                                        Low =[]
                                        Open =[]
                                        while Index2 < Index:
                                            Index2 = Index2 + 1
                                            Value2 = list(StepData.values())[Index2]
                                            Date.append(str(list(StepData.keys())[Index2]))
                                            Open.append(int(float(Value2.get("1. open"))))
                                            High.append(int(float(Value2.get("2. high"))))
                                            Low.append(int(float(Value2.get("3. low"))))
                                            Close.append(int(float(Value2.get("4. close"))))
                                        Date.reverse()
                                        Open.reverse()
                                        High.reverse()
                                        Low.reverse()
                                        Close.reverse()
                                        print(Open)
                                        print(Close)
                                        print(High)
                                        print(Low)
                                        print(Date)
                                        bar_chart = pygal.Bar(spacing=100, fill=True, x_label_rotation=20)
                                        bar_chart.title = (StockSymbol +' Stock Data')
                                        bar_chart.x_labels =('Red', 'Blue', 'Green', 'Yellow')
                                        bar_chart.x_labels = Date
                                        bar_chart.add('Open', Open)
                                        bar_chart.add('High', Close)
                                        bar_chart.add('Low', Low)
                                        bar_chart.add('close', Close)
                                        bar_chart.render_in_browser()
                                        break
                                        
                                    elif TimeSeries == 4:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&interval=30min'+ Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Time Series (30min)']
                                        Index = list(StepData).index(input('Please enter Start Date: '))
                                        Index2 = list(StepData).index(input('Please enter End Date: '))
                                        Value = list(StepData.values())[Index]
                                        Value2 = list(StepData.values())[Index2]
                                        Close =[]
                                        Date =[]
                                        High = []
                                        Low =[]
                                        Open =[]
                                        while Index2 < Index:
                                            Index2 = Index2 + 1
                                            Value2 = list(StepData.values())[Index2]
                                            Date.append(str(list(StepData.keys())[Index2]))
                                            Open.append(int(float(Value2.get("1. open"))))
                                            High.append(int(float(Value2.get("2. high"))))
                                            Low.append(int(float(Value2.get("3. low"))))
                                            Close.append(int(float(Value2.get("4. close"))))
                                        Date.reverse()
                                        Open.reverse()
                                        High.reverse()
                                        Low.reverse()
                                        Close.reverse()
                                        print(Open)
                                        print(Close)
                                        print(High)
                                        print(Low)
                                        print(Date)
                                        bar_chart = pygal.Bar(spacing=100, fill=True, x_label_rotation=20)
                                        bar_chart.title = (StockSymbol +' Stock Data')
                                        bar_chart.x_labels =('Red', 'Blue', 'Green', 'Yellow')
                                        bar_chart.x_labels = Date
                                        bar_chart.add('Open', Open)
                                        bar_chart.add('High', Close)
                                        bar_chart.add('Low', Low)
                                        bar_chart.add('close', Close)
                                        bar_chart.render_in_browser()
                                        break
                                except:
                                    print("Select the Time Series of the chart you want to Generate")
                                    print("-----------------------")
                                    print("1. Daily")
                                    print("2. Weekly")
                                    print("3. Monthly")
                                    print("4. Intraday") 
                                    print("Data Error Please Select Either '1','2','3', or '4': ")
                        elif ChartChoice == 2: 
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
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Time Series (Daily)']
                                        Index = list(StepData).index(input('Please enter Start Date: '))
                                        Index2 = list(StepData).index(input('Please enter End Date: '))
                                        Value = list(StepData.values())[Index]
                                        Value2 = list(StepData.values())[Index2]
                                        Close =[]
                                        Date =[]
                                        High = []
                                        Low =[]
                                        Open =[]
                                        while Index2 < Index:
                                            Index2 = Index2 + 1
                                            Value2 = list(StepData.values())[Index2]
                                            Date.append(str(list(StepData.keys())[Index2]))
                                            Open.append(int(float(Value2.get("1. open"))))
                                            High.append(int(float(Value2.get("2. high"))))
                                            Low.append(int(float(Value2.get("3. low"))))
                                            Close.append(int(float(Value2.get("4. close"))))
                                        Date.reverse()
                                        Open.reverse()
                                        High.reverse()
                                        Low.reverse()
                                        Close.reverse()
                                        print(Open)
                                        print(Close)
                                        print(High)
                                        print(Low)
                                        print(Date)
                                        line_chart = pygal.Line(spacing=100, fill=False, x_label_rotation=20)
                                        line_chart.title = (StockSymbol +' Stock Data')
                                        line_chart.x_labels =('Red', 'Blue', 'Green', 'Yellow')
                                        line_chart.x_labels = Date
                                        line_chart.add('Open', Open)
                                        line_chart.add('High', Close)
                                        line_chart.add('Low', Low)
                                        line_chart.add('close', Close)
                                        line_chart.render_in_browser()
                                        break

                                    elif TimeSeries == 2:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Weekly Time Series']
                                        Index = list(StepData).index(input('Please enter Start Date: '))
                                        Index2 = list(StepData).index(input('Please enter End Date: '))
                                        Value = list(StepData.values())[Index]
                                        Value2 = list(StepData.values())[Index2]
                                        Close =[]
                                        Date =[]
                                        High = []
                                        Low =[]
                                        Open =[]
                                        while Index2 < Index:
                                            Index2 = Index2 + 1
                                            Value2 = list(StepData.values())[Index2]
                                            Date.append(str(list(StepData.keys())[Index2]))
                                            Open.append(int(float(Value2.get("1. open"))))
                                            High.append(int(float(Value2.get("2. high"))))
                                            Low.append(int(float(Value2.get("3. low"))))
                                            Close.append(int(float(Value2.get("4. close"))))
                                        Date.reverse()
                                        Open.reverse()
                                        High.reverse()
                                        Low.reverse()
                                        Close.reverse()
                                        print(Open)
                                        print(Close)
                                        print(High)
                                        print(Low)
                                        print(Date)
                                        line_chart = pygal.Line(spacing=100, fill=False, x_label_rotation=20)
                                        line_chart.title = (StockSymbol +' Stock Data')
                                        line_chart.x_labels =('Red', 'Blue', 'Green', 'Yellow')
                                        line_chart.x_labels = Date
                                        line_chart.add('Open', Open)
                                        line_chart.add('High', Close)
                                        line_chart.add('Low', Low)
                                        line_chart.add('close', Close)
                                        line_chart.render_in_browser()
                                        break

                                    elif TimeSeries == 3:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Monthly Time Series']
                                        Index = list(StepData).index(input('Please enter Start Date: '))
                                        Index2 = list(StepData).index(input('Please enter End Date: '))
                                        Value = list(StepData.values())[Index]
                                        Value2 = list(StepData.values())[Index2]
                                        Close =[]
                                        Date =[]
                                        High = []
                                        Low =[]
                                        Open =[]
                                        while Index2 < Index:
                                            Index2 = Index2 + 1
                                            Value2 = list(StepData.values())[Index2]
                                            Date.append(str(list(StepData.keys())[Index2]))
                                            Open.append(int(float(Value2.get("1. open"))))
                                            High.append(int(float(Value2.get("2. high"))))
                                            Low.append(int(float(Value2.get("3. low"))))
                                            Close.append(int(float(Value2.get("4. close"))))
                                        Date.reverse()
                                        Open.reverse()
                                        High.reverse()
                                        Low.reverse()
                                        Close.reverse()
                                        print(Open)
                                        print(Close)
                                        print(High)
                                        print(Low)
                                        print(Date)
                                        line_chart = pygal.Line(spacing=100, fill=False, x_label_rotation=20)
                                        line_chart.title = (StockSymbol +' Stock Data')
                                        line_chart.x_labels =('Red', 'Blue', 'Green', 'Yellow')
                                        line_chart.x_labels = Date
                                        line_chart.add('Open', Open)
                                        line_chart.add('High', Close)
                                        line_chart.add('Low', Low)
                                        line_chart.add('close', Close)
                                        line_chart.render_in_browser()
                                    elif TimeSeries == 4:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&interval=30min'+ Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Time Series (30min)']
                                        Index = list(StepData).index(input('Please enter Start Date: '))
                                        Index2 = list(StepData).index(input('Please enter End Date: '))
                                        Value = list(StepData.values())[Index]
                                        Value2 = list(StepData.values())[Index2]
                                        Close =[]
                                        Date =[]
                                        High = []
                                        Low =[]
                                        Open =[]
                                        while Index2 < Index:
                                            Index2 = Index2 + 1
                                            Value2 = list(StepData.values())[Index2]
                                            Date.append(str(list(StepData.keys())[Index2]))
                                            Open.append(int(float(Value2.get("1. open"))))
                                            High.append(int(float(Value2.get("2. high"))))
                                            Low.append(int(float(Value2.get("3. low"))))
                                            Close.append(int(float(Value2.get("4. close"))))
                                        Date.reverse()
                                        Open.reverse()
                                        High.reverse()
                                        Low.reverse()
                                        Close.reverse()
                                        print(Open)
                                        print(Close)
                                        print(High)
                                        print(Low)
                                        print(Date)
                                        line_chart = pygal.Line(spacing=100, fill=False, x_label_rotation=20)
                                        line_chart.title = (StockSymbol +' Stock Data')
                                        line_chart.x_labels =('Red', 'Blue', 'Green', 'Yellow')
                                        line_chart.x_labels = Date
                                        line_chart.add('Open', Open)
                                        line_chart.add('High', Close)
                                        line_chart.add('Low', Low)
                                        line_chart.add('close', Close)
                                        line_chart.render_in_browser()
                                        break
                                except:
                                    print("Select the Time Series of the chart you want to Generate")
                                    print("-----------------------")
                                    print("1. Daily")
                                    print("2. Weekly")
                                    print("3. Monthly")
                                    print("4. Intraday") 
                                    print("Data Error Please Select Either '1','2','3', or '4': ")
                    except:
                        print("Chart Types")
                        print("-----------------------")
                        print("1. line")
                        print("2. Line")
                        print("Data Error Please Select Either '1' or '2': ")
                StockData = input("Would you like to view more stock data? Press 'y' to continue or 'n' to exit: ")
                if StockData !="y" and StockData !="n":
                    print("Error Data Type Invalid. Please enter 'y' or 'n': ")
                    StockData = input("Would you like to view more stock data? Press 'y' to continue or 'n' to exit: ")
                ChartChoice = 0
                StockSymbol = ""
                Symbol = ""
                TimeSeries = 0
StockFunc()
