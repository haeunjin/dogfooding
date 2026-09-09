Y = int(input())


if Y % 4 == 0: ## 4로 나누어 떨어지는 윤년이라면
    if (Y % 100 == 0) and (Y % 400 != 0): ## 윤년이지만 100으로 나누어 떨어지되 400으로 나누어 떨어지지 않으면
        print("false")
    else:
        print("true")

else:
    print("false")

