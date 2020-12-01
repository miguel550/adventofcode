
nums = []
with open('./day1.0.txt') as f:
    for n in f:
        nums.append(int(n))

for i, num in enumerate(nums):
    for j, num2 in enumerate(nums):
        if i == j:
            continue
        if num + num2 == 2020:
            print(num * num2)



