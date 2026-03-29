class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.compressedString = compressedString
        self.curChar = None
        self.curFreq = None

        if self.compressedString:
            self._parse_compressedString(self.compressedString)


    def _parse_compressedString(self, compressedString):
        """
        return two variable: char, freq
        """
        if not compressedString:
            self.curChar = None
            self.curFreq = None
            return

        self.curChar = compressedString[0]
        p = 1
        while p < len(compressedString) and compressedString[p].isdigit():
            p += 1

        self.curFreq = int(compressedString[1:p])
        self.compressedString = self.compressedString[p:]

    def next(self):
        """
        :rtype: str
        """
        if not self.curChar:
            return ' '

        res = self.curChar

        # update internal
        self.curFreq -= 1
        if not self.curFreq:
            self._parse_compressedString(self.compressedString)

        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curChar:
            return True

        return False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()