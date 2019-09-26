-- find-all-by-name
SELECT * FROM users WHERE name = :name

-- find-one-by-id
SELECT * FROM users WHERE id = 10 LIMIT 1

-- find-users-join-products
SELECT * FROM users u
    INNER JOIN products p ON u.id = p.user_id
    WHERE u.id = 1
    LIMIT 1