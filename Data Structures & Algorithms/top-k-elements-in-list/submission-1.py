class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.setdefault(num, 0) + 1
        tuples = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        result = [item[0] for item in tuples]
        return result[:k]