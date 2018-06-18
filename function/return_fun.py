def stu_register(name, age, course):

    print(name, age, course)

    if age > 22:
        return False
    else:
        return True


status = stu_register('Jason', 28, 'python')
print(status)
