def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
def find_anniversary(year, is_next):
    if is_next:
        while True:
            year += 1
            if is_leap_year(year):
                return year
    else:
        while True:
            year -= 1
            if is_leap_year(year):
                return year
year = int(input("Enter the year: "))
is_next = input("Is it the next anniversary? (yes/no): ").lower()
if is_next == 'yes':
    print("Next leap year anniversary:", find_anniversary(year, True))
elif is_next == 'no':
    print("Previous leap year anniversary:", find_anniversary(year, False))
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
