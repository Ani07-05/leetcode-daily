class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        all = self.permute(cards)
        for a,b,c,d in all:
            a = a * 1.0
            b = b * 1.0
            c = c * 1.0
            d = d * 1.0
            # 2 and 2
            st = [a + b, a - b, a * b, a / b]
            rd = [c + d, c - d, c * d, c / d]
            for s in st:
                for r in rd:
                    if abs(s + r - 24) < 0.1:
                        return True
                    elif abs(s - r - 24) < 0.1 or abs(r - s - 24) < 0.1:
                        return True
                    elif abs(s * r - 24) < 0.1:
                        return True
                    elif (r != 0 and abs(s / r - 24) < 0.1) or (s != 0 and abs(r / s - 24) < 0.1):
                        return True
            # 1 and 3
            first = [a+b, a-b, a*b, a/b]
            second = []
            for i in first:
                second.append(c + i)
                second.append(c - i)
                second.append(i - c)
                second.append(c * i)
                if i != 0:
                    second.append(c + i)
                if c != 0:
                    second.append(c + i)
            for j in second:
                if abs(j + d - 24) < 0.1:
                    return True
                elif abs(j - d - 24) < 0.1 or abs(d - j - 24) < 0.1:
                    return True
                elif abs(j * d - 24) < 0.1:
                    return True
                elif (d != 0 and abs(j / d - 24) < 0.1) or (j != 0 and abs(d / j - 24) < 0.1):
                    return True
        

        return False





    def permute(self, nums):
        if len(nums) == 0:
            return [[]]
        res = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            for p in self.permute(rest):
                res.append([nums[i]] + p)
        return res
        