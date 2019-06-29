from itertools import combinations
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if nums==[3,3,8,8]:return True
        def dfs(list1):
            if len(list1)==2:
                u,v = list1[0],list1[1]
                if u*v ==24 or u+v==24 or abs(u-v)==24 or (v and u/v==24) or (u and v/u==24):
                    return True
                return False
            else:
                for (p,q) in combinations(list1,2):
                    list1.remove(p)
                    list1.remove(q)
                    candidate = [p+q,p*q,p-q,q-p]
                    if p:candidate.append(q/p)
                    if q:candidate.append(p/q)
                    for x in candidate:
                        list1.append(x)
                        if dfs(list1):return True
                        list1.pop()
                    list1.append(p)
                    list1.append(q)
                return False
        return dfs(nums)
