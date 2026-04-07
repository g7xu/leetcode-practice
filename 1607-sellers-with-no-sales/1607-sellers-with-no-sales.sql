-- Write your PostgreSQL query statement below
WITH etc as (
    SELECT seller_id, seller_name, 2020 as YEAR
    FROM Seller as s
)

SELECT SELLER_NAME
FROM etc 
LEFT JOIN Orders as o ON o.seller_id = etc.seller_id AND etc.year = DATE_PART('year', o.sale_date)
WHERE o.order_id is NULL
ORDER BY SELLER_NAME ASC