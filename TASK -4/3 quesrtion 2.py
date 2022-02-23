lst = []
n = int(input("Input number of elements : "))
print("Enter the serial number , name and marks respectively to output a data table")
for i in range(0, n):
    ele = [input(), input(),input()]
    lst.append(ele)
print("input the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for i in range(3):
    print(lst[1][i], end=" "*10)