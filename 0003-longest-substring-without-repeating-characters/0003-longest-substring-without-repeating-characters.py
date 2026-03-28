class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        char_collection = set()
        curr_length = 0
        max_length = 0

        slow, fast = 0, 0

        while fast < len(s):
            
            
            if s[fast] in char_collection:
                char_collection.remove(s[slow])
                slow += 1
                continue
        

            char_collection.add(s[fast])
            curr_length = fast - slow + 1
            max_length = max(curr_length, max_length)
            fast += 1

        return max_length
        