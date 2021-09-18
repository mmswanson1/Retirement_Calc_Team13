def calculate_age(birth_year):
    birth_year = int(birth_year)

    if birth_year <= 1937:
        age_year = 65
        age_month = 0
    elif 1942 >= birth_year > 1937:
        age_year = 65
        age_month = (birth_year - 1937) * 2
    elif 1954 >= birth_year >= 1943:
        age_year = 66
        age_month = 0
    elif 1959 >= birth_year >= 1955:
        age_year = 66
        age_month = (birth_year - 1954) * 2
    else:
        age_year = 67
        age_month = 0

    return age_year, age_month


def display_month(months, birth_month):
    retire_month = birth_month + months
    if retire_month > 12:
        retire_month -= 12

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']

    return month_list[retire_month - 1]


def calculate_year(birth_year, years, birth_month, retire_month):
    retire_year = int(birth_year) + years
    if (birth_month + retire_month) > 12:
        retire_year += 1

    return retire_year
