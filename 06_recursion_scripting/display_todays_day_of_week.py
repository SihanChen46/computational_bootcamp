"Print today's day of the week"

from datetime import date

if __name__ == '__main__':  
    day_of_week = date.today().strftime('%a')
    print(day_of_week)   
