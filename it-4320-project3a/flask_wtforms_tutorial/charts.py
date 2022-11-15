'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime
from datetime import date
import pygal

ChartChoice = 0
ChartType = ['pygal.Bar(fill=True)', 'pygal.Line(fill=False)']
DateChoice = ''
Date = '&date=' + DateChoice
Close =[]
Date =[]
High = []
Low =[]
Open =[]
Function = ['function=TIME_SERIES_DAILY','function=TIME_SERIES_WEEKLY','function=TIME_SERIES_MONTHLY','function=TIME_SERIES_INTRADAY']
StockData = 'y'
StockSymbol = ''
Symbol = ''
TimeSeries = 0
StepData = ''
IntraInterval = ['interval=1min','interval=5min','interval=15min','interval=30min','interval=60min']
def PopChartIntra():
    global StepData
    global Close
    global Date
    global High
    global Low
    global Open
    global Input
    global SecondInput

    try: 
        DateInfo=(input('Please enter Start Date (YYYY-MM-DD): '))
        HourInfo=(input('Please enter Start Time (HH:MM:SS): '))
        Input = str(DateInfo+ ' '+ HourInfo)
        while Input =='':
            Input=(input('Please enter Start Date (YYYY-MM-DD): '))
        if (Input in list(StepData)):
            Index = list(StepData).index(Input)
        else:
            while (Input in list(StepData)) == False:
                HourArray = HourInfo.split(':')
                HourNum=int(HourArray[0])
                MinNum = int(HourArray[1])
                if MinNum == 60:
                    HourNum = HourNum+1
                    MinNum = 00
                    HourInfo = (str(HourNum).zfill(2) + ':' + str(MinNum).zfill(2)+ ':' + HourArray[2])
                    Input = str(DateInfo+ ' '+ HourInfo)
                else:
                    MinNum = MinNum +1
                    HourInfo = (str(HourNum).zfill(2) + ':' + str(MinNum).zfill(2)+ ':' + HourArray[2])
                    Input = (DateInfo+ ' '+ str(HourNum)+ ':' + str(MinNum).zfill(2)+ ':' + HourArray[2])
                
            Index = list(StepData).index(Input)

        DateInfo=(input('Please enter End Date (YYYY-MM-DD): '))
        HourInfo=(input('Please enter End Time (HH:MM:SS): '))
        SecondInput = str(DateInfo+ ' '+ HourInfo)
        print(SecondInput)
        while SecondInput =='':
            SecondInput=(input('Please enter End Date (YYYY-MM-DD): '))
        if (SecondInput in list(StepData)):
            Index2 = list(StepData).index(SecondInput)
        else:
            while (SecondInput in list(StepData)) == False:
                HourArray = HourInfo.split(':')
                HourNum=int(HourArray[0])
                MinNum = int(HourArray[1])
                if MinNum == 00:
                    HourNum = HourNum-1
                    MinNum = 60
                    HourInfo = (str(HourNum).zfill(2) + ':' + str(MinNum).zfill(2)+ ':' + HourArray[2])
                    SecondInput = str(DateInfo+ ' '+ HourInfo)
                else:
                    MinNum = MinNum - 1
                    HourInfo = (str(HourNum).zfill(2) + ':' + str(MinNum).zfill(2)+ ':' + HourArray[2])
                    SecondInput = (DateInfo+ ' ' + str(HourNum)+ ':' + str(MinNum).zfill(2)+ ':' + HourArray[2])
        Index2 = list(StepData).index(SecondInput)

        if Index > Index2:
            Value = list(StepData.values())[Index2]
            while Index2-1 < Index:
                Value = list(StepData.values())[Index2]
                Date.append(str(list(StepData.keys())[Index2]))
                Open.append(int(float(Value.get('1. open'))))
                High.append(int(float(Value.get('2. high'))))
                Low.append(int(float(Value.get('3. low'))))
                Close.append(int(float(Value.get('4. close'))))
                Index2 = Index2 + 1
            Date.reverse()
            Open.reverse()
            High.reverse()
            Low.reverse()
            Close.reverse()
        else:
           print('Error Start Date must be eariler than End Date please re-enter: ')
    except:
     print('error with Data Entry')
    
def PopChart():
    global StepData
    global Close
    global Date
    global High
    global Low
    global Open
    global Input
    global SecondInput

    try: 
        Input=(input('Please enter Start Date (YYYY-MM-DD): '))
        while Input =='':
            Input=(input('Please enter Start Date (YYYY-MM-DD): '))
        if Input =='':
            print('Please enter Start Date (YYYY-MM-DD): ')
        else:
            if (Input in list(StepData)):
                Index = list(StepData).index(Input)
            else:
                while (Input in list(StepData)) == False:
                    dateArray = Input.split('-')
                    DayNum = int(dateArray[2])
                    MonthNum = int(dateArray[1])
                    if DayNum == 31:
                        DayNum = 0
                        MonthNum = MonthNum + 1
                        Input = (dateArray[0] + '-' + str(MonthNum).zfill(2) + '-' + str(DayNum).zfill(2))
                    else:
                
                        DayNum = DayNum + 1
                        Input = (dateArray[0] + '-' + str(MonthNum).zfill(2) + '-' + str(DayNum).zfill(2))
                Index = list(StepData).index(Input)
        SecondInput=(input('Please enter End Date (YYYY-MM-DD): '))
        while SecondInput =='':
            SecondInput=(input('Please enter End Date (YYYY-MM-DD): '))
        if SecondInput =='':
            print('Please enter Start Date (YYYY-MM-DD): ')
        else:
            if (SecondInput in list(StepData)):
                Index2 = list(StepData).index(SecondInput)
            else:
                while (SecondInput in list(StepData)) == False:
                    dateArray = SecondInput.split('-')
                    DayNum = int(dateArray[2])
                    MonthNum = int(dateArray[1])
                    if DayNum == 00:
                        DayNum = 31
                        MonthNum = MonthNum - 1
                        SecondInput = (dateArray[0] + '-' + str(MonthNum).zfill(2) + '-' + str(DayNum).zfill(2))
                    else:
                        DayNum = DayNum - 1
                        SecondInput = (dateArray[0] + '-' + str(MonthNum).zfill(2) + '-' + str(DayNum).zfill(2))
                Index2 = list(StepData).index(SecondInput)

        if Index > Index2:
            Value = list(StepData.values())[Index2]
            while Index2-1 < Index:
                Value = list(StepData.values())[Index2]
                Date.append(str(list(StepData.keys())[Index2]))
                Open.append(int(float(Value.get('1. open'))))
                High.append(int(float(Value.get('2. high'))))
                Low.append(int(float(Value.get('3. low'))))
                Close.append(int(float(Value.get('4. close'))))
                Index2 = Index2 + 1
            Date.reverse()
            Open.reverse()
            High.reverse()
            Low.reverse()
            Close.reverse()
        else:
           print('Error Start Date must be eariler than End Date please re-enter: ')
    except:
     print('error with Data Entry')
def BarChart():
    global StockSymbol
    global Close
    global Date
    global High
    global Low
    global Open
    global Input
    global SecondInput
    bar_chart = pygal.Bar(spacing=100, fill=True, x_label_rotation=40)
    bar_chart.title = ('Stock Data for '+ StockSymbol.upper() + ': ' + Input +' to ' + SecondInput)
    bar_chart.x_labels =('Red', 'Blue', 'Green', 'Yellow')
    bar_chart.x_labels = Date
    bar_chart.add('Open', Open)
    bar_chart.add('High', Close)
    bar_chart.add('Low', Low)
    bar_chart.add('close', Close)
    bar_chart.render_in_browser()

def LineChart():
    global StockSymbol
    global Close
    global Date
    global High
    global Low
    global Open
    global Input
    global SecondInput
    line_chart = pygal.Line(spacing=100, fill=False, x_label_rotation=40)
    line_chart.title = ('Stock Data for '+ StockSymbol.upper() + ': ' + Input +' to ' + SecondInput)
    line_chart.x_labels =('Red', 'Blue', 'Green', 'Yellow')
    line_chart.x_labels = Date
    line_chart.add('Open', Open)
    line_chart.add('High', Close)
    line_chart.add('Low', Low)
    line_chart.add('close', Close)
    line_chart.render_in_browser()

def StockFunc():
    global ChartChoice
    global ChartType
    global Symbol
    global StockSymbol
    global StockData
    global TimeSeries
    global StepData

    print('Stock Data Visualizer')
    print('-----------------------')
    while StockData != 'n':
            StockSymbol = input('Enter the stock symbol you are looking for: ')
            if StockSymbol == '':
                print('No Data Entry')
            else:
                Symbol = '&symbol='+ StockSymbol
                print('Your Symbol was' + Symbol)
                while ChartChoice != 1 and ChartChoice != 2:
                    try:
                        print('Chart Types')
                        print('-----------------------')
                        print('1. Bar')
                        print('2. Line')
                        ChartChoice = int(input('Enter the chart type you want (1, 2): '))
                        if ChartChoice == 1:
                            while TimeSeries != 1 and TimeSeries != 2 and TimeSeries != 3 and TimeSeries != 4:
                                try:
                                    print('Select the Time Series of the chart you want to Generate')
                                    print('-----------------------')
                                    print('1. Daily')
                                    print('2. Weekly')
                                    print('3. Monthly')
                                    print('4. Intraday')     
                                    TimeSeries = int(input('Enter time series option (1, 2, 3, 4): '))
                                    if TimeSeries == 1:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Time Series (Daily)']
                                        PopChart()
                                        BarChart()
                                        break

                                    elif TimeSeries == 2:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Weekly Time Series']
                                        PopChart()
                                        BarChart()
                                        break
                                    
                                    elif TimeSeries == 3:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Monthly Time Series']
                                        PopChart()
                                        BarChart()
                                        break
                                        
                                    elif TimeSeries == 4:
                                        print('Select the Intevals you want your chart to generate')
                                        print('-----------------------')
                                        print('1. 1 Minute')
                                        print('2. 5 Minute')
                                        print('3. 15 Minute')
                                        print('4. 30 Minute')   
                                        print('5. 60 Minute') 
                                        IntervalSeries = int(input('Enter time series option (1, 2, 3, 4, 5): '))
                                        while IntervalSeries != 1 and IntervalSeries != 2 and IntervalSeries != 3 and IntervalSeries != 4 and IntervalSeries != 5:
                                            try:
                                                print('Select the Intevals you want your chart to generate')
                                                print('-----------------------')
                                                print('1. 1 Minute')
                                                print('2. 5 Minute')
                                                print('3. 15 Minute')
                                                print('4. 30 Minute')   
                                                print('4. 60 Minute') 
                                            except:
                                                print('Data Error')   
                                        if IntervalSeries == 1:
                                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1]+'&'+IntraInterval[IntervalSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                            DataDic = requests.get(URL)
                                            data = DataDic.json()
                                            print(URL)
                                            StepData = data['Time Series (1min)']
                                            PopChartIntra()
                                            BarChart()
                                            break

                                        elif IntervalSeries == 2:
                                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1]+'&'+IntraInterval[IntervalSeries-1] +  Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                            DataDic = requests.get(URL)
                                            data = DataDic.json()
                                            print(URL)
                                            StepData = data['Time Series (5min)']
                                            PopChartIntra()
                                            BarChart()
                                            break

                                        elif IntervalSeries == 3:
                                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&'+IntraInterval[IntervalSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                            DataDic = requests.get(URL)
                                            data = DataDic.json()
                                            print(URL)
                                            StepData = data['Time Series (15min)']
                                            PopChartIntra()
                                            BarChart()
                                            break

                                        elif IntervalSeries == 4:
                                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&'+IntraInterval[IntervalSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                            DataDic = requests.get(URL)
                                            data = DataDic.json()
                                            print(URL)
                                            StepData = data['Time Series (30min)']
                                            PopChartIntra()
                                            BarChart()
                                            break

                                        elif IntervalSeries == 5:
                                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&'+IntraInterval[IntervalSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                            DataDic = requests.get(URL)
                                            data = DataDic.json()
                                            print(URL)
                                            StepData = data['Time Series (60min)']
                                            PopChartIntra()
                                            BarChart()
                                            break
                                except:
                                    print('Select the Time Series of the chart you want to Generate')
                                    print('-----------------------')
                                    print('1. Daily')
                                    print('2. Weekly')
                                    print('3. Monthly')
                                    print('4. Intraday') 
                                    print("Data Error Please Select Either '1','2','3', or '4': ")
                        elif ChartChoice == 2: 
                            while TimeSeries != 1 and TimeSeries != 2 and TimeSeries != 3 and TimeSeries != 4:
                                try:
                                    print('Select the Time Series of the chart you want to Generate')
                                    print('-----------------------')
                                    print('1. Daily')
                                    print('2. Weekly')
                                    print('3. Monthly')
                                    print('4. Intraday')     
                                    TimeSeries = int(input('Enter time series option (1, 2, 3, 4): '))
                                    if TimeSeries == 1:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Time Series (Daily)']
                                        PopChart()
                                        LineChart()
                                        break

                                    elif TimeSeries == 2:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Weekly Time Series']
                                        PopChart()
                                        LineChart()
                                        break

                                    elif TimeSeries == 3:
                                        URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                        DataDic = requests.get(URL)
                                        data = DataDic.json()
                                        StepData = data['Monthly Time Series']
                                        PopChart()
                                        LineChart()
                                    elif TimeSeries == 4:
                                        print('Select the Intevals you want your chart to generate')
                                        print('-----------------------')
                                        print('1. 1 Minute')
                                        print('2. 5 Minute')
                                        print('3. 15 Minute')
                                        print('4. 30 Minute')   
                                        print('5. 60 Minute') 
                                        IntervalSeries = int(input('Enter time series option (1, 2, 3, 4, 5): '))
                                        while IntervalSeries != 1 and IntervalSeries != 2 and IntervalSeries != 3 and IntervalSeries != 4 and IntervalSeries != 5:
                                            try:
                                                print('Select the Intevals you want your chart to generate')
                                                print('-----------------------')
                                                print('1. 1 Minute')
                                                print('2. 5 Minute')
                                                print('3. 15 Minute')
                                                print('4. 30 Minute')   
                                                print('5. 60 Minute') 
                                            except:
                                                print('Data Error')   
                                        if IntervalSeries == 1:
                                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1]+'&'+IntraInterval[IntervalSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                            DataDic = requests.get(URL)
                                            data = DataDic.json()
                                            print(URL)
                                            StepData = data['Time Series (1min)']
                                            PopChartIntra()
                                            LineChart()
                                            break

                                        elif IntervalSeries == 2:
                                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1]+'&'+IntraInterval[IntervalSeries-1] +  Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                            DataDic = requests.get(URL)
                                            data = DataDic.json()
                                            print(URL)
                                            StepData = data['Time Series (5min)']
                                            PopChartIntra()
                                            LineChart()
                                            break

                                        elif IntervalSeries == 3:
                                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&'+IntraInterval[IntervalSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                            DataDic = requests.get(URL)
                                            data = DataDic.json()
                                            print(URL)
                                            StepData = data['Time Series (15min)']
                                            PopChartIntra()
                                            LineChart()
                                            break

                                        elif IntervalSeries == 4:
                                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&'+IntraInterval[IntervalSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                            DataDic = requests.get(URL)
                                            data = DataDic.json()
                                            print(URL)
                                            StepData = data['Time Series (30min)']
                                            PopChartIntra()
                                            LineChart()
                                            break
                                        
                                        elif IntervalSeries == 5:
                                            URL = 'https://www.alphavantage.co/query?'+ Function[TimeSeries-1] +'&'+IntraInterval[IntervalSeries-1] + Symbol +'&apikey=7CKUYMD19R6Q9LKW'
                                            DataDic = requests.get(URL)
                                            data = DataDic.json()
                                            print(URL)
                                            StepData = data['Time Series (60min)']
                                            PopChartIntra()
                                            LineChart()
                                            break    
                                except:
                                    print('Select the Time Series of the chart you want to Generate')
                                    print('-----------------------')
                                    print('1. Daily')
                                    print('2. Weekly')
                                    print('3. Monthly')
                                    print('4. Intraday') 
                                    print("Data Error Please Select Either '1','2','3', or '4': ")
                    except:
                        print('Chart Types')
                        print('-----------------------')
                        print('1. line')
                        print('2. Line')
                        print("Data Error Please Select Either '1' or '2': ")
                StockData = input("Would you like to view more stock data? Press 'y' to continue or 'n' to exit: ")
                if StockData !='y' and StockData !='n':
                    print("Error Data Type Invalid. Please enter 'y' or 'n': ")
                    StockData = input("Would you like to view more stock data? Press 'y' to continue or 'n' to exit: ")
                ChartChoice = 0
                StockSymbol = ''
                Symbol = ''
                TimeSeries = 0
                Close.clear()
                Date.clear()
                High.clear()
                Low.clear()
                Open.clear()

StockFunc()

#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()

