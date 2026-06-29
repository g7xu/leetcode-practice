class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(height, name) for name, height in zip(names, heights)]

        return [name for _, name in sorted(people, reverse = True)]