# def multi(a=0, b=4):
#     if (type(a) is not int or type(b)is not int):
#         return
#     return a + b
# multi(3,4)
# multi(6,7)
# total = multi(7, 8)
# print(total)  

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("sara", 1, True, 6+7j)
def dict (**kwargs):
    print(kwargs)
    print(type(kwargs))
dict(marv = 13, john = 12)
