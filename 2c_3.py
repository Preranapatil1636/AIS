nums = [1,4,-5,-20,10]
sum = 0

for i in range(len(nums)):
    if nums[i] > 0:
        sum += nums[i]

print(sum)