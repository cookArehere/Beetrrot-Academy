"""
Task 1

The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

     “Good day <name>! <day> is a perfect day to learn some python.”
Note that <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.

"""
task1 = '{:^65}'.format('Task 1')
print(task1)
print()
#1
name = 'Oleg'
day = 'Monday'

method_one = "Good day " +  name + "! " + day + " is a perfect day to learn some python."
print("method_one: " + method_one)

#2
information = {'name': 'Andry', 'day': 'Tuesday'}

method_two = 'Good day {name}! {day} is a perfect day to learn some python.'.format(**information)
print("method_two: " + method_two)

#3
method_three = 'Good day {0}! {1} is a perfect day to learn some python.'.format("Vika", "Wednesday")
print("method_three: " + method_three)
print()

"""
Task 2

Manipulate strings.

Save your first and last name as separate variables, then use string concatenation 
to add them together with a white space in between and print a greeting.

"""
task2 = '{:^65}'.format('Task 2')
print(task2)
print()

my_name = "Pavel"
my_last_name = "Kunpan"

print('Hello ' + my_name + ' ' + my_last_name, end="!")
print()

"""
Task 3

Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 

Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division

"""
task3 = '{:^65}'.format('Task 3')
print(task3)
print()

a = 2
b = 10

print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a ** b)
print(a % b)
print(a // b)
print()

"""
Task 4

доп задания (под звездочкой)

вариант задания осваивать форматирование строк. Заполните прочерк чтобы получить вот такую строку на выходе. 
обратите внимание что 110110 это двоичное представление числа. То есть в строке выведен int, str, int, float но второй инт выведен в виде битовом

"000012 Василий 110110 32.10"

 

print("____________________".format(12, "Василий", 54, 32.1))

 

Попробуйте взять какое то одно слово в переменную и "собрать" из него другие слова. Выведите по разному, капсом, маленькими, с отступами. 

Например взяли слово "Корован"  

s1 = "Корован"

подумайте как вы из него можете вывести слово "ворона"


"""
task4 = '{:^65}'.format('Task 4')
print(task4)
print()

#print("____________________".format(12, "Василий", 54, 32.1))
print('{0:0>6} {1:s} {2:b} {3:g}'.format(12, "Василий", 54, 32.1))

vorona = '{4}{3}{2}{1}{6}{5}'.format(*'Корован')
print(vorona)
print(vorona.capitalize())
print(vorona.upper())


