from application.salary import *
from application.db.people import *
from application.circle import *
from datetime import datetime

if name == 'main':

date = datetime.now()  
formatted_date = date.strftime("%d-%m-%Y в %H:%M:%S")

calculate_salary(formatted_date)
get_employees(formatted_date)

circle(2, 2, 5)
