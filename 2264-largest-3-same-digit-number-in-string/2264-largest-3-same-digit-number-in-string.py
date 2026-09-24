class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""


        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if not res:
                    res = num[i:i+3]

                if int(num[i:i+3]) > int(res):
                    res = num[i:i+3]

                if res == "999":
                    return res


        return res

            