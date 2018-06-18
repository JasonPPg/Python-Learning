num = int(input("Please input your number:"))

if num <= 100 and num >= 90:
    print("A")
elif num < 90 and num >= 80:
    print("B")
elif num < 80 and num >= 60:
    print("C")
else:
    print("不及格")
