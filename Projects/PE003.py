# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

a = 600851475143
total = 1
result = []
for i in range(1,a+1):
    if a % i == 0:
        result.append(i)
        total = i * total
        if total == a:
            break

print(result)
print(total)