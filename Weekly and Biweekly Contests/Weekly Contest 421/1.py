# 3334. Find the maximum factor score of an array

import math
from functools import reduce
from operator import mul

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        def prime_decomposition(num):
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
            i = 0
            result = []
            while num>1:
                if num%primes[i] == 0:
                    result.append(primes[i])
                    num = num/primes[i]
                    i -= 1
                i += 1
            return result
        
        def remove_redundant_sublists(prime_factorizations):
            max_count = {}
            for sublist in prime_factorizations:
                for prime in set(sublist):
                    count = sublist.count(prime)
                    if prime not in max_count or count > max_count[prime]:
                        max_count[prime] = count
            filtered_list = [sublist for sublist in prime_factorizations if all(sublist.count(prime) == max_count[prime] for prime in set(sublist))]
            return filtered_list     
               
        def calculate_gcd(l):
            return reduce(math.gcd, l)
        
        def calculate_lcm(l):
            def lcm(a, b):
                return a*b // math.gcd(a, b)
            return reduce(lcm, l, 1)
        
        def calculate_factor_score(numbers, prime_factorization):
            original_gcd = calculate_gcd(numbers)
            original_lcm = calculate_lcm(numbers)
            best = original_gcd * original_lcm
            for i, num in enumerate(numbers):
                new_numbers = numbers[:i] + numbers[i+1:]
                if new_numbers:
                    new_gcd = calculate_gcd(new_numbers)
                    new_lcm = calculate_lcm(new_numbers)
                    new_factor_score = new_gcd * new_lcm
                else:
                    new_factor_score = 0
                if new_factor_score > best:
                    best = new_factor_score
            return best
        
        allPrimes = []
        for num in nums:
            current = prime_decomposition(num)
            allPrimes.append(current)
        significant_primes = remove_redundant_sublists(allPrimes)
        answer = calculate_factor_score(nums, significant_primes)
        return answer
    
answer = Solution()
maxScore = answer.maxScore(nums = [3])
print(f"Max Score: {maxScore}")