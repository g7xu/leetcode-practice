# we can represent each word in terms of a string of 26 length
# create a hashmap for the group
# key is the string representation
# value is the list of words


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def find_key(s):
            bucket = [0] * 26
            for char in s:
                bucket[ord(char) - ord('a')] += 1

            # print(bucket)

            return ','.join([str(i) for i in bucket])

        group = dict()

        for s in strs:
            key = find_key(s)
            print(key)

            if key in group:
                group[key].append(s)
            else:
                group[key] = [s]

        # print(group)
        return list(group.values())

            


        
        