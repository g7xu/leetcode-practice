class Logger(object):

    COOLDOWN = 10

    def __init__(self):
        self.record = dict()
        self.COOLDOWN = 10
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.record or timestamp >= self.record[message]:
            self.record[message] = timestamp + self.COOLDOWN
            return True

        return False


    
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)