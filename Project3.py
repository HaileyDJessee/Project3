def getStartDate(data, startDate):
    try:
        return list(data).index(startDate)
    except:
        dateArray = startDate.split('-')
        dateNum = int(dateArray[2])
        if dateNum == 31:
            dateNum = 1
        else:
            dateNum = dateNum + 1
        getStartDate(data, dateArray[0] + '-' + dateArray[1] + '-' + str(dateNum))

def getEndDate(data, endDate):
    try:
        return list(data).index(endDate)
    except:
        dateArray = endDate.split('-')
        dateNum = int(dateArray[2])
        if dateNum == 1:
            dateNum = 31
        else:
            dateNum = dateNum - 1
        getEndDate(data, dateArray[0] + '-' + dateArray[1] + '-' + str(dateNum))
        
#How to use:
# Index = list(StepData).index(getStartDate(StepData, input('Please enter Start Date: ')))
# Index2 = list(StepData).index(getEndDate(StepData, input('Please enter End Date: ')))
