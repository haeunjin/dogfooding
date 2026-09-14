A, B, C = map(int, input().split())


#A가 중앙값인 경우(B<A<C or C<A<B)
#B가 중앙값인 경우
#C가 중앙값인 경우

if (B<A and A<C) or (C<A and A<B):
    print(A)
elif (A<B and B<C) or (C<B and B<A):
    print(B)
else:
    print(C)


# if A가 중앙값인 조건:
#     print(A)

# elif B가 중앙값인 조건:
#     print(B)

# else:
#     print(C)