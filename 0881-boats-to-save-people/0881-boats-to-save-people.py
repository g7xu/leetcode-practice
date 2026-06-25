class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        head = 0
        tail = len(people) - 1

        res = 0
        while head <= tail:
            if people[tail] + people[head] > limit:
                res += 1
                tail -= 1
            else:
                res += 1
                tail -= 1
                head += 1


        if head == tail:
            return res + 1 

        return res
            