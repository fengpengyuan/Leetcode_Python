import math

__author__ = 'fengpeng'


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in xrange(n + 1):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, x):
        if x < 2:
            return False
        for i in xrange(2, x / 2):
            if x % i == 0:
                return False
        return True


    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        for i in xrange(2, int(math.sqrt(n))+1):
            if primes[i]:
                for j in xrange(2 * i, n, i):
                    primes[j] = False
        count = 0
        for i in xrange(2, n):
            if primes[i]:
                count += 1
        return count


print Solution().countPrimes2(7)