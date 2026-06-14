def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        return "Error: 0 is not ddevisable"
    except TypeError:
        return "Error: Give integer"
    else:
        return f"Result: {result}"
    finally:
        print("Divide() function called")

print(divide(10,2))
print(divide(10,0))
print(divide(10,"abc"))
