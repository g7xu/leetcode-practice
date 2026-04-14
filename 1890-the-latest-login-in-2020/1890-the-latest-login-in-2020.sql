-- Write your PostgreSQL query statement below
SELECT l.user_id, MAX(l.time_stamp) as last_stamp
FROM Logins as l
WHERE DATE_PART('year', l.time_stamp) = 2020
GROUP BY l.user_id
