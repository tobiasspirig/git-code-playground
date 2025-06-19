class JustnotCoolError(Exception):
    pass

x = 2
try:
    # print(x/0  )
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
    raise JustnotCoolError ("This is not okay!")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Please do not divide by 0.")
except Exception as error:
    print(error)
else:
    print("No errors!")
finally: 
    print("I am going to print with or without an error.")

