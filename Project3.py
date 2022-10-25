print("Stock Data Visualizer")
print("-----------------------")

StockSymbol = input("Enter the stock symbol you are looking for: ")

print("Chart Types")
print("-----------------------")
print("1. Bar")
print("2. Line")

ChartType = input("Enter the chart type you want (1, 2):")

print("Select the Time Series of the chart you want to Generate")
print("-----------------------")
print("1. Intraday")
print("2. Daily")
print("3. Weekly")
print("4. Monthly")

TimeSeries = input("Enter time series option (1, 2, 3, 4):")

StartDate = input("Enter the start date (YYYY-MM-DD):")

EndDate = input("Enter the end date (YYYY-MM-DD):")

MoreData = input("Would you like to view more stock data? Press 'y' to continue: ")
