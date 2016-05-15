__author__ = 'fengpeng'


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0 or denominator == 0:
            return "0"
        dict = {}
        res = ""
        if numerator * denominator < 0:
            res += "-"

        numerator = abs(numerator)
        denominator = abs(denominator)
        qo = numerator / denominator
        rem = numerator % denominator
        res += str(qo)
        if rem == 0:
            return res
        res += "."
        while rem != 0 and rem not in dict:
            dict[rem] = len(res)
            numerator = rem * 10
            qo = numerator / denominator
            rem = numerator % denominator
            res += str(qo)

        if rem == 0:
            return res
        index = dict.get(rem)
        res = res[:index] + "(" + res[index:] + ")"
        return res

    def fractionToDecimal2(self, numerator, denominator):
        if numerator == 0 or denominator == 0:
            return "0"
        res = []
        if numerator * denominator < 0:
            res.append("-")
        num, den = abs(numerator), abs(denominator)
        q, rem = divmod(num, den)
        res.append(str(q))
        if rem == 0:
            return "".join(res)
        res.append(".")
        dict = {}
        while rem:
            if rem in dict:
                res.insert(dict[rem], "(")
                res.append(")")
                return "".join(res)
            dict[rem] = len(res)
            q, rem = divmod(rem * 10, den)
            res.append(str(q))
        return "".join(res)


print Solution().fractionToDecimal(22, 3)
print Solution().fractionToDecimal2(22, 3)

