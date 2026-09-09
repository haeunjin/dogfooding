n = int(input())

#윤년이 아닌 해에 n월은 며칠이 있는가?
#윤년이 아닌 해의 2월은 28일까지 있음.

#만약 1월이면 31일, 2월이면 28일까지 있음.

# 2월 -> 28일
# 4,6,9,11월 -> 30일
# 나머지 -> 31일

# if n == 4 and n == 6 and n == 9 and n == 11:


if n != 2:
    if n == 4 or n == 6 or n == 9 or n == 11:
        print(30)
    else:
        print(31)
else:
    print(28)
    