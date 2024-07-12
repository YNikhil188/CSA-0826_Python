def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def next_anniversary(year):
    return year + (4 if is_leap_year(year) else 1)

def previous_anniversary(year):
    return year - (4 if is_leap_year(year) else 1)

def find_anniversary_leap_year(year):
    if is_leap_year(year):
        print("The given year {} is a leap year.".format(year))
        print("Next leap year anniversary:", next_anniversary(year))
    else:
        print("The given year {} is not a leap year.".format(year))
        print("Previous leap year anniversary:", previous_anniversary(year))

# Sample Input
year = int(input("Enter the year of the anniversary: "))
find_anniversary_leap_year(year)