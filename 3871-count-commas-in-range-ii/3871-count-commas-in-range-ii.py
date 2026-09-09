r""" Thinking area

length:
1 -> 0
2 -> 0
3 -> 0
4 ->
  -> % [last digit]000 
  -> 1000 * num // 1000

  - 1000


1,234,567


we should think this way, number greater than this, should contains at least one commas so 

"""

class Solution:
    def countCommas(self, n: int) -> int:
        p = 1000
        res = 0
        
        while p <= n:
            res += n - p + 1
            p *= 1000

        return res