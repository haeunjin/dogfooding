x = input().split()
x_cold = x[0]
x_tem = int(x[1])

y = input().split()
y_cold = y[0]
y_tem = int(y[1])

z = input().split()
z_cold = z[0]
z_tem = int(z[1])


# 한 번에 3명씩 검사. x,y,z 중 2명이 증상이 있고 체온이 37도 이상이면 위급.
#x,y / x,z / y,z

if x_cold =="Y" and x_tem >=37:
    if y_cold =="Y" and y_tem >=37:
        print("E")
    elif z_cold =="Y" and z_tem >=37:
        print("E")
    else:
        print("N")


elif y_cold =="Y" and y_tem >=37:
    if z_cold =="Y" and z_tem >=37:
        print("E")
    else:
        print("N")

elif x_cold =="Y" and x_tem >=37:
    if y_cold =="Y" and y_tem >=37:
        if z_cold =="Y" and z_tem >=37:
            print("E")
        else:
            print("N")

else:
    print("N")