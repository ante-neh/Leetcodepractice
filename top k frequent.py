class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        res = []
        for i in range (len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] = dic[nums[i]]+ 1
        sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
        length = len(sorted_dic) - 1
        while k > 0:
            res.append(sorted_dic[length][0] )
            length -= 1
            k -= 1
        return res