# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# 1부터 1000까지 입력
# 3의 배수, 5의 배수를 각각 변수에 담기
# 3과 5의 공동배수는 한번만 담기

result = 0
for i in range(1000):
    if i % 3 == 0:
        result += i
    elif i % 5 == 0:
        result += i
    elif i % 15 == 0:
        result = result - i
    else:
        pass
print(result)


# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         result += i
# print(result)