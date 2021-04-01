def date_julian(year):
    a = year % 4
    b = year % 7
    c = year % 19
    d = (19*c+15) % 30
    e = (2*a+4*b-d+34) % 7
    month = (d+e+114) // 31
    day = ((d+e+114) % 31) + 1
    month_greg = 0
    day_greg = 0
    
    if month == 3:
        if day + 13 > 31:
            day_greg = day - 18
            month_greg = month + 1
        else:
            day_greg = day +13
            month_greg = month
    elif month == 4:
        if day + 13 > 30:
            day_greg = day - 17
            month_greg = month +1
        else:
            day_greg = day + 13
            month_greg = month

    if month == 3:
        print("{}. ožujka {}. po julijanskom kalendaru".format(day, year))
    elif month == 4:
        print("{}. travnja {}. po julijanskom kalendaru".format(day, year))
    elif month == 5:
        print("{}. svibnja {}. po julijanskom kalendaru".format(day, year))

    if month_greg == 3:
        print("{}. ožujka {}. po gregorijanskom kalendaru".format(day_greg, year))
    elif month_greg == 4:
        print("{}. travnja {}. po gregorijanskom kalendaru".format(day_greg, year))
    elif month_greg == 5:
        print("{}. svibnja {}. po gregorijanskom kalendaru".format(day_greg, year))

year = int(input("Unesite godinu za koju želite saznati datum pravoslavnog Uskrsa: "))
print()
date_julian(year)