class Solution:
    def __init__(self):
        self.ans = []

    def subset_sum(self, A,i,sum_, curr_sum, p):
        if p:
            if sum(curr_sum) == sum_:
                if curr_sum not in self.ans:
                    self.ans.append(curr_sum)
        if sum(curr_sum) > sum_: return 0
        if i == len(A):
            if sum(curr_sum) == sum_:
                return 1
            else:
                return 0

        take = self.subset_sum(A, i+1, sum_, curr_sum + [A[i]], True)
        dont = self.subset_sum(A, i+1, sum_, curr_sum, False)
        return take + dont

    def Solve(self,A,B):
        A.sort()
        self.subset_sum(A, 0, B, [], False)
        return self.ans

if __name__ == '__main__':
    A = [10, 1, 2, 7, 6, 1, 5]
    B = 8
    C = Solution()
    print(C.Solve(A,B))
