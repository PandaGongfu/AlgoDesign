
import bisect

fh = open('2sum.txt', 'r')
lines = fh.read().split('\n')

nums = []
for l in lines[:-1]:
    nums.append(int(l))

nums = list(set(nums))
nums.sort()
num_dict = {}
for num in nums:
    num_dict[num] = 1

WIDTH = 10000
out = set()
for i in nums:
    lower = bisect.bisect_left(nums, -WIDTH - i)
    upper = bisect.bisect_right(nums, WIDTH - i)
    out |= set([i + j for j in nums[lower:upper]])

len(out)



