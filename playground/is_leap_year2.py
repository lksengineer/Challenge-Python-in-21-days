def is_leap_year(year):
    """Function is leap year"""
    if year % 1 != 0 or year <= 0:
        return False
    
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return True
    return False

if __name__ == '__main__':
    year = -2024
    print(is_leap_year(year))