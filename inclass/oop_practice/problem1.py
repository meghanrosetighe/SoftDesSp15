""" A practice problem for object-oriented programming """

class Date(object):
    """ Represents a particular day on the calendar """
    def __init__(self, month, day, year):
        """ Initializes a Date object

            month: the month (represented as an integer in [1,12])
            day: the day of the month (represented as an integer)
            year: the year (represented as an integer)
            This method will not validate whether a given date is invalid
            (e.g. April 31, 2000) """
        
        self.month = month
        self.day = day
        self.year = year


    def is_before(self,other_date):
        """ Returns true if and only if self occurs before other_date

            >>> d1 = Date(4,20,1981)
            >>> d2 = Date(5,31,1995)
            >>> d1.is_before(d2)
            True
        """
        if self.year < other_date.year:
            return True
        elif self.year > other_date.year:
            return False
        else:
            if self.month < other_date.month:
                return True
            elif self.month > other_date.month:
                return False
            else:
                return self.day < other_date.day


    def __str__(self):
        """ Converts the date to a string in the following format:
            Month, Day Year (where Month is the name of the month, e.g. January)

        >>> print Date(3,26,2015)
        March, 26th 2015
        """
        Months = {1:'January', 2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
        if self.day ==1 or self.day ==21 or self.day==31:
            printable_date = Months[self.month] + ", " + str(self.day) + "st " + str(self.year)
        elif self.day ==2 or self.day==22:
            printable_date = Months[self.month] + ", " + str(self.day) + "nd " + str(self.year)
        elif self.day==3:
            printable_date = Months[self.month] + ", " + str(self.day) + "rd " + str(self.year)
        else:
            printable_date = Months[self.month] + ", " + str(self.day) + "th " + str(self.year)
        return printable_date

    def increment_year(self):
        """ Modifies the Date object self so that it represents a date of the
            same month and day but for the following year. 
            >>> d1 = Date(9,22,1994)
            >>> print d1.increment_year()
            September, 22nd 1995
            """
        self.year +=1
        return self

    def is_leap_year(self):
        """ Returns true if the year that this date falls in is a leap year
            see: http://en.wikipedia.org/wiki/Leap_year

            Note: please add appropriate doctests BEFORE you start coding 

            >>> d1 = Date(3,26,2015)
            >>> print d1.is_leap_year()
            False

            >>> d1 = Date(3,26,1904)
            >>> print d1.is_leap_year()
            True
            """
        if self.year %4 != 0:
            return False
        elif self.year %100 != 0:
            return True
        elif self.year%400 != 0:
            return False
        else:
            return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()