class Solution:
    def bestClosingTime(self, customers: str) -> int:
        posFix_Y = [0]

        for i in range(len(customers) - 1, -1, -1):
            
            posFix_Y.append(posFix_Y[-1] + (1 if customers[i] == 'Y' else 0))

        posFix_Y = posFix_Y[::-1]


        preFix_N = [0]

        for i in range(len(customers)):
            preFix_N.append(preFix_N[-1] + (1 if customers[i] == 'N' else 0))


        print(posFix_Y)
        print(preFix_N)


        res_min = len(customers)
        res = None
        for i in range(len(posFix_Y)):
            tmp = posFix_Y[i] + preFix_N[i]

            if res_min > tmp:
                res = i
                res_min = tmp


        return res
