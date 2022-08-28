class Solution:
    def answerQueries(self, nums, queries):
        ans = []
        results = []
        ret = 0
        nums = sorted(nums)
        for num in nums:
            ret += num
            results.append(ret)
        for querie in queries:
            for index in range(len(results)):
                if querie < results[index]:
                    break
            if querie > results[index]:
                ans.append(index+1)
            else:
                ans.append(index)
            # print(querie,results[index])
            # print(index)
        return ans
# nums = [4,5,2,1]
nums = [2,3,4,5]
# queries = [3,10,21]
queries = [1]
ans = Solution().answerQueries(nums, queries)
print(ans)