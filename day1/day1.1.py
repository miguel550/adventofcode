
nums = []
with open('./day1.0.txt') as f:
    for n in f:
        nums.append(int(n))

for i, num in enumerate(nums):
    for j, num2 in enumerate(nums):
        if i == j:
            continue
        for k, num3 in enumerate(nums):
            if j == k or k == i:
                continue
            if num + num2 + num3 == 2020:
                print(num * num2 * num3)



