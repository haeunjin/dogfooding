a = input()
arr = a.split()

a_age=int(arr[0])
a_gender = arr[1]

b = input()
arr = b.split()

b_age=int(arr[0])
b_gender = arr[1]

if (a_age >= 19 and a_gender == "M") or (b_age >= 19 and b_gender == "M"):
    print(1)
else:
    print(0)