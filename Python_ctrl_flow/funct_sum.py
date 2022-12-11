def Work():
    numberWork = int(input("Inter a number:: "))
    sum = numberWork + 10
    for all in range(sum):
        print(all)


Work()


def grades(Alevel, Blevel, Clevel):
    result = Alevel + Blevel + Clevel
    return result


print(" Result is:: ", grades(20, 40, 20))
