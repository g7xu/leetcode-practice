class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        M = len(words)
        N = max([len(word) for word in words])

        if M != N:
            return False

        
        for i in range(M):
            for j in range(N):
                if j >= len(words[i]) and i >= len(words[j]):
                    continue

                if j >= len(words[i]) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    print(i, j)
                    return False

        return True

        # ab, bnrt, crm