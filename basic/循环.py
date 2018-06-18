# -*- coding: utf-8 -*-

count = 0

while count <= 100:

    if count == 50:
        pass
    elif count <= 80 and count >= 60:
        print("loop", count * count)
    else:
        print("loop", count)
    count += 1
print("end")
