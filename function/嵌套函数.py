age = 10


def func1():
    global age

    def func2():
        print(age)

    func2()
    age = 11


func1()
