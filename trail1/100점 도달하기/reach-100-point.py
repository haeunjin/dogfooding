n = int(input())


for i in range(n, 101, +1):
    if i >= 90:
        print("A", end=" ")
    elif i >= 80:
        print("B", end=" ")
    elif i >= 70:
        print("C", end=" ")
    elif i >= 60:
        print("D", end=" ")
    else:
        print("F", end=" ")


# i=1

# while n <= 100:
#     if i >= 90:
#         print("A")
#     elif i >= 80:
#         print("B")
#     elif i >= 70:
#         print("C")
#     elif i >= 60:
#         print("D")
#     else:
#         print("F")
#     n += 1
    