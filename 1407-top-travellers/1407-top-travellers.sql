-- Write your PostgreSQL query statement below

SELECT u.name, COALESCE(SUM(r.distance), 0) as travelled_distance
FROM Users as u
LEFT JOIN Rides as r ON r.user_id = u.id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC