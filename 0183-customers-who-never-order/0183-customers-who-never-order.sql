-- Write your PostgreSQL query statement below
SELECT name as Customers
FROM Customers as c
WHERE NOT EXISTS (SELECT customerId from Orders as o where c.id = o.customerId)