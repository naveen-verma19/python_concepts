def multiply(a,*numbers):
    """
    Here numbers are received not as list but as a TUPLE
    """
    a=1
    print(type(numbers)) #tuple
    for num in numbers:
        a*=num
    return a

p=multiply(3,2,3,4,5)
print(p)


def get_user(*nums,**user):
    """
    :param nums: tuple
    :param user: dictionary
    """
    print(nums)
    for k,v in user.items():
        print(k,v)

get_user(1,2,3,4,5,6,7,id=1,name='joseph',phone=1234)


