# Custome error
class InvalidAgeError(Exception):
    def __init__(self,message):
        super().__init__(message)
        
def set_Age(age):
    if age<0 or age>99:
        raise InvalidAgeError(f"{age} is not valid age")
    return age

try:
    set_Age(-99)
except InvalidAgeError as e:
    print(f"Custome Error: {e}")
    
    # new error
class InvalidNumError(Exception):
    def __init__(self,message):
        super().__init__(message)

def set_num(num):
    if num<0 or num>99:
        raise InvalidNumError(f"{num} is not valid")
    return num

try:
    set_num(-10)
except InvalidNumError as e:
    print(f"Custome Error: {e}")