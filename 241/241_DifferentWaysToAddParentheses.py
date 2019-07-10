class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        # 分治问题
        # Time: 24ms
        res = []
        for i, c in enumerate(input):
            if c in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            res.append(int(l) + int(r))
                        elif c == '-':
                            res.append(int(l) - int(r))
                        else:
                            res.append(int(l) * int(r))

        if not res:
            res.append(int(input))

        return res
