class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i, num1 in enumerate(nums[:(len(nums)-1)]):
    #         for j, num2 in enumerate(nums[i+1:], start=i+1):
    #             if target - num1 == num2:
    #                 return [i,j]
    #     return []
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}
        for i, num in enumerate(nums):
            current_list: List[int] | None  = value_index.get(num)
            if current_list:
                value_index[num] = current_list + [i]
            else:
                value_index[num] = [i] 
        
        for i, num in enumerate(nums):
            matchy_list = value_index.get(target - num)
            if matchy_list:
                for j in matchy_list:
                    if i != j:
                        return [i,j]
        return []