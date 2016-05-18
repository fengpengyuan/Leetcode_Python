__author__ = 'fengpeng'


class Solution(object):
    belowTen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    belowTwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                   "Nineteen"]
    belowHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        return self.helper(num)


    def helper(self, num):
        res = ""
        if num < 10:
            return self.belowTen[num]
        if num < 20:
            return self.belowTwenty[num - 10]
        if num < 100:
            res = self.belowHundred[num / 10] + " " + self.helper(num % 10)
        elif num < 1000:
            res = self.belowTen[num / 100] + " Hundred " + self.helper(num % 100)
        elif num < 1000000:
            res = self.helper(num / 1000) + " Thousand " + self.helper(num % 1000)
        elif num < 1000000000:
            res = self.helper(num / 1000000) + " Million " + self.helper(num % 1000000)
        else:
            res = self.helper(num / 1000000000) + " Billion " + self.helper(num % 1000000000)
        return res.strip()

    LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                    "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords2(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        res, i = "", 0
        while num > 0:
            if num % 1000 != 0:
                res = self.convert(num % 1000) + self.THOUSANDS[i] + " " + res
            num /= 1000
            i += 1
        return res.strip()

    def convert(self, num):
        if num == 0:
            return ""
        if num < 20:
            return self.LESS_THAN_20[num]+" "
        if num < 100:
            return self.TENS[num / 10] + " " + self.convert(num % 10)
        if num < 1000:
            return self.LESS_THAN_20[num / 100] + " Hundred " + self.convert(num % 100)


print Solution().numberToWords(50868)
print Solution().numberToWords(50868)