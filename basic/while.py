count = 1

while count < 4:

    age = int(input("Please input your age"))

    if age != 22:
        print("wrong!!")
    else:
        print("right!!")
        break
    count += 1

    if count == 4:
        choise = input("继续？y|Y")
        if choise == 'y' or choise == 'Y':
            count = 0
        else:
            print("错误的选择！！")