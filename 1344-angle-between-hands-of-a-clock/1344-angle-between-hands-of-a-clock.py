# track the percentage as we go

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_percentage = minutes / 60
        hr_percentage = hour / 12 + min_percentage * (1/12)

        gap = abs(min_percentage - hr_percentage)
        angle_one = gap * 360

        print(min(angle_one, 360 - angle_one))
        return min(angle_one, 360 - angle_one)
        