try:
    x = 5/2
except ZeroDivisionError:
    print("Error")
else:
    print("Else Block: Result = ", x)
finally:
    print("Finally runs")
