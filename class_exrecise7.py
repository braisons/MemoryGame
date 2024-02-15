# wirte a program to determine which ex 4
# results is greater calulate the remainder for
# fl = 2**2 * x - (3 * x) + 1
# f2 = 2 * x + 3 * x + 3
# where
# x = 1, 2, 3


for nun in range(3):
    x = int(input(" Enter the value of x "))
    f1 = 2**2 * x - (3 * x) + 1
    f2 = 2 * x + 3 * x + 3

    if f1 > f2:
        print("f1 is greater")
    else:
         print("f2 is greater")
