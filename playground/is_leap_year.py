def is_leap_year(year):
    """Function is leap year"""
    if not isinstance(year, int) or year <= 0:
        return False

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


if __name__ == '__main__':
    year = "2024"
    print(is_leap_year(year))
