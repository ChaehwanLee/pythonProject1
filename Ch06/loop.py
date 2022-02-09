# 1~10 까지의 합을 구하시오
# for 문을 이용하시오

# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)

sum = 0;
for i in range(1,11):
    sum += i;
print(sum);

# while 문을 이용하시오

# sum = 0
# while
#     if sum > 1 and i <=10:
#         sum = sum + i
#         break
#     print(sum)

sum2 = 0;
i = 1;
while i <= 10:
    sum2 += i;
    i += 1;
print(sum2);