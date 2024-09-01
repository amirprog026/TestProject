a=2
b=input("please enter a number")
if b.isnumeric():
    print(a**int(b))
else:
    raise Exception("ERROR on data. Please only Enter numeric value")