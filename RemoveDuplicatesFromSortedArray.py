nums = list(map(int,input().split()))
x=len(nums)
nums = list(set(nums))
for i in range(len(nums),x):
    nums.append("_")
print(x,nums)