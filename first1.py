#Luluh Almogbil
'''
# LAB_EXCEPTIONS


## Below you have a code that raises an exception , using what you learned do the following:
- Find what type of exception is raised. Name error
- Hanlde the exception in try..except 
- If operation successful , print "the operation is successful"
- if operation fails, handle the specific exception that is raised , and print a relevant message.
```
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


additoin(10, 20)
'''


def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


try:
    additoin(10, 20)
    print("the operation is successful")
except NameError as e:
    print("This is a name error exception, vars are not compatable")
except Exception as e:
    print(e.__class__)
















# def additoin(x, y):
#     try:
#         x = 10
#         y = 20
#         print("Addition:", x + b)  # 'b' is not defined, this will raise NameError
#         print("the operation is successful")
#     except NameError:
#         print("error: used a variable that isn't defined (NameError).")

# additoin(10, 20)






