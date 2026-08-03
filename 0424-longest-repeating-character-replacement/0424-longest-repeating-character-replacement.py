# sliding window

# expand when same char or has k left

# reduce when no k and different char

# extend when we can

# shrink when we can't

# hashmap
# MaxHeap

from heapq import heappop, heappush

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = collections.defaultdict(int)
        maxHeap = []
        res = 1
        slow = fast = 0

        def updateHeap(maxHeap, freq):
            while -maxHeap[0][0] != freq[maxHeap[0][1]]:
                heappop(maxHeap)


        while fast < len(s):
            freq[s[fast]] += 1
            heappush(maxHeap, (-freq[s[fast]], s[fast]))
            updateHeap(maxHeap, freq)

            while fast - slow + 1 + maxHeap[0][0] > k:
                freq[s[slow]] -= 1
                heappush(maxHeap, (-freq[s[slow]], s[slow]))
                updateHeap(maxHeap, freq)
                slow += 1

            res = max(res, fast - slow + 1)
            fast += 1

        return res
                

        