# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    # daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def is_leap(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
                
    def days(year, month, day):
        
        daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        if is_leap(year):
            daysOfMonths[1] = 29
        else:
            daysOfMonths[1] = 28
        
        def getDays(month1, day1):
            days = 0
            i = 0
            while i < month1 -1:
                days = days + daysOfMonths[i]
                i = i + 1
            days = days + day1
            return days
        return getDays(month, day)
        
    # 注意 1900 2100 这些非闰年陷阱，其前后三年，共七年，都是非闰年，365天    
    def daysOBetweenYears(yearBirth, yearNow):
        daysBetweenYears = 0
        for year in range(yearBirth, yearNow):
            if is_leap(year):
                daysBetweenYears += 366
            else:
                daysBetweenYears += 365
        return daysBetweenYears
    
    return days(year2, month2, day2) - days(year1, month1, day1) + daysOBetweenYears(year1, year2)      



# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523),
                  ((1899,12,31,1900,1,1),1)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

# print daysBetweenDates(2012,1,1,2012,2,28)