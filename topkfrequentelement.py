class Solution:
    def topKFrequent(self, nums, k: int):
        num_map = {}
        sorted_freq = {}
        result = []
        
        # build frequency map of nums
        for num in nums:
            if num not in num_map:
                num_map[num] = 0
            num_map[num] += 1
        
        # sort keys of frequency map in ascending order
        sorted_keys = sorted(num_map, key=num_map.get)
        
        # build new sorted dict
        for key in sorted_keys:
            sorted_freq[key] = num_map[key]
        
        # append top K keys to result
        for i in range(k):
            result.append(sorted_freq.popitem()[0])
        
        return result
    