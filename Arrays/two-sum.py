def twoSum(nums: list[int], target: int) -> list[int]:
    result = list()
    for i in nums:
        for j in nums:
            if i + j == target and i != j:
                result.extend([nums.index(i), nums.index(j)])
                return result