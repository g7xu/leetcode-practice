class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            change = arr[:]
            changed = False
            for i in range(1, len(arr) - 1):
                l = arr[i - 1]
                m = arr[i]
                r = arr[i + 1]
                if m < l and m < r:
                    change[i] += 1
                    changed = True
                elif m > l and m > r:
                    change[i] += -1
                    changed = True
            
            if not changed:
                return arr

            arr = change