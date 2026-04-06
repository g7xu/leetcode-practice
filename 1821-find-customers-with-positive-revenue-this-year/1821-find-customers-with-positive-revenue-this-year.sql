-- Write your PostgreSQL query statement below
SELECT customer_id
from Customers as c
WHERE c.revenue > 0 and year = 2021