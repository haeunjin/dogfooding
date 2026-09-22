inp = input()
arr = inp.split()

N = int(arr[0])
a = int(arr[1])

i=1

while i <= N:
    if i % a == 0:
        print(1)
    else:
        print(0)
    i += 1