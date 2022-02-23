lst = []
n = int(input("INPUT NUMBER OF ROWS : "))
print("Enter the Serial number , name and marks respectively to output a data table")
for i in range(0, n):
    ele = [input(), input(),input()]
    lst.append(ele)
print("Input the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for a in lst:
    for b in a:
        print(b,end=" "*10)
    print()