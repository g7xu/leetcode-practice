class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        head = 0
        tail = len(people) - 1

        res = 0
        while head <= tail:
            res += 1
            if people[tail] + people[head] <= limit:    
                head += 1
            tail -= 1
                


        return res
            