from typing import List

nums = [1, 2, 2, 4]
seen = set()
duplicate_number = -1
missing_number = -1

for index in range(1, len(nums)):
    if nums[index] in seen:
        duplicate_number = nums[index]
    seen.add(nums[index])

    if index not in nums:
        missing_number = index
