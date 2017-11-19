
# created by andre, ray, malcolm, roman on nov 2017
# generates random numbers then finds the average

import ui
from numpy import random

my_numbers =[] 

def calculate_average(my_numbers_list):
    total = 0
    
    for number , value in enumerate(my_numbers , 0):
        total = total + value
        number = number + 1
        
    average = float(total/ number)
    return float(average)
    
def create_10_random_number(number_list = []):
     for random_numbers in range(10):
         random_numbers = random.randint(1,100)
         my_numbers.append(random_numbers)
     view['generate_label'].text = "the numbers are: " + str(my_numbers)
def generate (sender):
    create_10_random_number()  
def calculate(sender):
   answer = calculate_average(my_numbers)
   view['average_label'].text ="the average is: " + str(answer)


view = ui.load_view()
view.present('sheet')



