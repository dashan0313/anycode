给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answers =  []
        n = len(candidates)
        candidates.sort()

        def back(start,t,tmp):
            if t == 0: #终止条件
                answers.append(tmp)
                return
            for k in range(start,n):
                if candidates[k] > t:
                    continue
                if k > start and candidates[k] == candidates[k-1]:
                    continue
                #如果在树的同一层，就用第一个阿
                #注意不要写成tmp = tmp + [candidates[k]],那样全局设置就变了
                #同理，也不要写成tmp.append()，和上面结果一样的！
                back(k + 1,t - candidates[k],tmp + [candidates[k]])

        back(0,target,[])
        return answers
