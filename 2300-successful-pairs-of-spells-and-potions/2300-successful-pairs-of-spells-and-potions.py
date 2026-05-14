# binary search

# left if >= success
# right if < success

# n log m

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def find(spell, potions, success):
            l = 0
            r = len(potions) - 1
            

            while r - l > 1:
                m = (l + r) // 2

                if potions[m] * spell >= success:
                    r = m - 1
                else:
                    l = m

            # possibility of all them them qualified
            if potions[l] * spell >= success:
                return len(potions)

            if potions[r] * spell < success:
                return len(potions) - r - 1
            else:
                return len(potions) - l - 1

        potions = sorted(potions)
        res = []
        for spell in spells:
            res.append(find(spell, potions, success))

        return res 