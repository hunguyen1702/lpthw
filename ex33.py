def range_rewrite(maximum, numbers_list, inc):
    i = 0
    while i < maximum:
        print "At the top i is %d" % i
        numbers_list.append(i)

        i += inc
        print "Numbers now: ", numbers_list
        print "At the bottom i is %d" % i


def change_list(numbers_list):
    # if we go with 1st line after this, nothing happen
    # numbers_list = [0, 0, 0]
    numbers_list[:]  = []



numbers = []
range_rewrite(10, numbers, 2)


print "The numbers:"

for num in numbers:
    print num


change_list(numbers)


print "The numbers:"

for num in numbers:
    print num
