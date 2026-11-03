"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        i_id = dict()
        for idx, employee in enumerate(employees):
            i_id[employee.id] = idx


        def helper(id, employees):
            if not employees[i_id[id]].subordinates:
                return employees[i_id[id]].importance

            res = employees[i_id[id]].importance
            for de in employees[i_id[id]].subordinates:
                res += helper(de, employees)

            return res

        return helper(id, employees)
