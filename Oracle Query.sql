-- 1. How many users are there?

SELECT COUNT(*) AS user_count
FROM users;

-- 2. Every user has made how many requests?

SELECT u.user_id, u.username, COUNT(r.request_id) AS request_count
FROM users u
JOIN requests r ON u.user_id = r.user_id
GROUP BY u.user_id, u.username
ORDER BY request_count DESC;

-- 3. Display total number of successful request?

SELECT COUNT(*) AS successful_request_count
FROM requests
WHERE status = 'SUCCESS';
