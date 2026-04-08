class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = dict()
        magazine_dict = dict()

        for char in ransomNote:
            if char not in ransomNote_dict:
                ransomNote_dict[char] = 1
            else:
                ransomNote_dict[char] += 1

        for char in magazine:
            if char not in magazine_dict:
                magazine_dict[char] = 1
            else:
                magazine_dict[char] += 1

        for letter, am_needed in ransomNote_dict.items():
            if letter in magazine_dict and magazine_dict[letter] >= am_needed:
                continue
            
            return False

        return True