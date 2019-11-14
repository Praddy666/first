d = input('What is your name? ')
f = input ('What is the name of your school? ')
g = input ('Where do you stay? ')
print ('Hello! My name is '+ d +". The name of my school is "+ f +'. I live at '+ g + '.') 
mar = input('Marks per Paper\n(excluding histoy and geography): ')
b = int(mar)*6
marks = input ('How much did you score in maths? ')
marks1 = input ('how much did you score in science? ')
marks2 = input ('how much did you score in english? ')
marks3 = input ('how much did you score in hindi? ')
marks4 = input ('how much did you score in third lang? ')
marks5 = input ('how much did you score in social science? ')
a = (int(marks) + int(marks1)+ int(marks2)+ int(marks3)+ int(marks4)+int(marks5) )/int(b) * 100 
print('Your percentage is ' + str(a) )
