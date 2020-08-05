给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。回溯算法
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers =  []
        candidates.sort()
        n = len(candidates)

        def back(i,tmp_sum,tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                answers.append(tmp)
                return
            back(i,tmp_sum + candidates[i],tmp+[candidates[i]])
            back(i+1,tmp_sum,tmp)
        back(0,0,[])
        return answers



JAVA遍历N叉树结点

public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }

    private static void backtrack(List<List<Integer>> result, List<Integer> cur, int candidates[], int target, int start) {
        if (target == 0) {
            result.add(new ArrayList<>(cur));
            return;
        }
        //相当于遍历N叉树的子节点
        for (int i = start; i < candidates.length; i++) {
            //如果当前节点大于target我们就不要选了
            if (target < candidates[i])
                continue;
            //由于在java中List是引用传递，所以这里要重新创建一个
            List<Integer> list = new ArrayList<>(cur);
            list.add(candidates[i]);
            backtrack(result, list, candidates, target - candidates[i], i);
        }
    }

作者：sdwwld
链接：https://leetcode-cn.com/problems/combination-sum/solution/di-gui-hui-su-tu-wen-fen-xi-ji-bai-liao-9987de-yon/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers =  []
        n = len(candidates)

        def back(start,t,tmp):
            if t == 0:
                answers.append(tmp)
                return
            for k in range(start,n):
                if candidates[k] > t:
                    continue
                #注意不要写成tmp = tmp + [candidates[k]],那样全局设置就变了
                back(k,t - candidates[k],tmp + [candidates[k]])

        back(0,target,[])
        return answers
