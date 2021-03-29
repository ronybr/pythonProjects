"""
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.
Sample Output:
25
48
"""
# num = 10
# func_lambda = lambda x: x + 15
# print(func_lambda(num))

# multip_lambda = lambda x,y: x * y
# print(multip_lambda(6,8))
###############
"""
Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
# list_tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print("Original list of tuples:")
# print(list_tuples)
# list_tuples.sort(key=lambda x: x[1])
# print("Sorted list of tuples:")
# print(list_tuples)
###############
"""
Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, 
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""
# list_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#             {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# print("Original list of dictionaries :")
# print(list_dict)
# list_dict_sorted = sorted(list_dict, key=lambda x: x["make"])
# print("Sorting the List of dictionaries :")
# print(list_dict_sorted)
###############
"""
Write a Python program to square and cube every number in a given list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""
# nums = range(1, 11)
# square_nums = list(map(lambda x: x ** 2, nums))
# cube_nums = list(map(lambda x: x ** 3, nums))
# print(str(square_nums) + "\n" + str(cube_nums))
###############
"""
Write a Python program to find if a given string starts with a given character using Lambda.
"""
#starts_with = lambda x: True if x.startswith("P") else False
#print(starts_with("python"))
###############
"""
Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
"""
#import datetime
#now = datetime.datetime.now()
#year = lambda x: x.year
#month = lambda x: x.month
#day = lambda x: x.day
#t = lambda x: x.time()
#print(now)
#print(year(now))
#print(month(now))
#print(day(now))
#print(t(now))
###############
"""
Write a Python program to check whether a given string is number or not using Lambda. 
"""
#list_nums = [1.65, 876554, -987.6, "A877", "UHGF", "001", 100]
#is_num = lambda x: str(x).replace(".", "", 1).isdigit()
#is_num1 = list(map(lambda x: is_num(str(x)[1:]) if str(x)[0] == "-" else is_num(x), list_nums))
#print(is_num1)
###############
"""
Write a Python program that multiply each number of given list with a given number using lambda function.
Print the result.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22
"""
#num = int(input("Informe um numero para ser multiplicado: "))
#init_list = [2, 4, 6, 9, 11]
#multi_func = list(map(lambda x: x * num, init_list))
#print(multi_func)
###############