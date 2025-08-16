class solution:
    def maximum69number (self, num):
        numlist = list(str(num))
        for i, c in enumerate(numlist):
            if c == '6':
                numlist[i] = '9'
                break
        modnum = "".join(numlist)
        return int(modnum)

#s = solution()
#print(s.maximum69number(9669))

