import time


def years_to_100(age):
    current_year = int(time.strftime("%Y"))
    year_if_100 = current_year +(100-int(age))
    return year_if_100
name = input("What is your name ?")
age = input("How old are you ?")

year_when_100 = years_to_100(age)
print("Hello {}, your age is : {} and you will turn 100 yers old: {} ".format(name,age,year_when_100))