-- Write your PostgreSQL query statement below
WITH t1 AS (
    SELECT o.customer_id
    FROM Orders as o
    GROUP BY o.customer_id
    HAVING 'A' = ANY(SELECT DISTINCT product_name FROM Orders as o1 where o1.customer_id = o.customer_id)
    AND 'B' = ANY(SELECT DISTINCT product_name FROM Orders as o1 where o1.customer_id = o.customer_id)
    AND 'C' != ALL(SELECT DISTINCT product_name FROM Orders as o1 where o1.customer_id = o.customer_id)
)

SELECT t1.customer_id, c.customer_name
FROM t1
LEFT JOIN Customers as c ON t1.customer_id = c.customer_id
ORDER BY t1.customer_id

