# basic structure of try/except
# try:
    # code that might crash
    # result = 10/0
# except:
    # if program crash except block gets active
    # print("0 is not devisable")
    

#! Multiple Exceptions
# try:
#     number = int(input("Enter an Integer: "))
#     result = 100/number
#     print(number)
# except ValueError:
#     print("not number")
# except ZeroDivisionError:
#     print("0 is not devisable")

#! finally exception
# try:
#     result = 10/2
# except ZeroDivisionError:
#     print("Error!")
# else:
#     print(f"result: {result}")
# finally:
#     print("Exception Ends! ")

