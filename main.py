from application.db.people import People
from application.salary import Salary
from _datetime import datetime
import wikipedia

if __name__ == '__main__':

    print(datetime.today().strftime('%d-%m-%Y'))

    People.get_employees()

    Salary.calculate_salary()

    print(wikipedia.summary('"Hello, world" program', sentences=3))



