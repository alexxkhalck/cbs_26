from db_connetor import get_connection


select_1 ="""
SELECT * FROM students;
"""

select_2 ="""
SELECT id, email FROM students;
"""

select_2_2 ="""
SELECT id, email FROM students
LIMIT 3
;
"""

select_3 ="""
SELECT id, email FROM students
WHERE email LIKE '%@gmail.com';
"""

"""
SELECT * FROM users WHERE id = 1;              -- Рівність
SELECT * FROM users WHERE id != 1;             -- Не рівно
SELECT * FROM users WHERE id <> 1;             -- Альтернатива для !=
SELECT * FROM users WHERE age > 18;            -- Більше
SELECT * FROM users WHERE age >= 18;           -- Більше або рівно
SELECT * FROM users WHERE age < 30;            -- Менше
SELECT * FROM users WHERE balance <= 1000;     -- Менше або рівно
"""
"""
-- AND (обидва умови повинні бути TRUE)
SELECT * FROM users WHERE is_active = TRUE AND age > 18;

-- OR (одна з умов повинна бути TRUE)
SELECT * FROM users WHERE is_active = FALSE OR balance < 100;
"""
"""
SELECT * FROM users WHERE id IN (1, 2, 3, 5);
SELECT * FROM users WHERE username IN ('ivan', 'maria', 'petro');
"""
select_4 ="""
SELECT * FROM students WHERE id IN (1, 2, 3, 5);
"""
"""
SELECT * FROM users WHERE age BETWEEN 18 AND 65;
SELECT * FROM users WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
"""
"""
SELECT * FROM users WHERE phone IS NULL;
"""

select_5 = """
SELECT * FROM students WHERE id IN (1, 2, 3, 5)
ORDER BY last_name DESC;
"""

"""
SELECT
    *.table_1,
    *.table_2
FROM table_1
INNER JOIN table_2
    ON table_1.id = table_2.user_id;
"""

select_join_1 = """
SELECT
    title, first_name, last_name, email
FROM courses
JOIN teachers
    ON courses.teacher_id = teachers.id;
"""

insert_couse = """
INSERT INTO courses
(title)
VALUES ('Python for Developer 2026 with AI')
"""
insert_teacher = """
INSERT INTO teachers
(first_name, last_name, email)
VALUES ('Ivan', 'Ivanov', 'ii@gmail.com')
"""

select_join_left = """
SELECT
    title, first_name, last_name, email
FROM courses
LEFT JOIN teachers
    ON courses.teacher_id = teachers.id
WHERE teachers.id IS NULL;
"""


select_join_right = """
SELECT
    title, first_name, last_name, email
FROM courses
RIGHT JOIN teachers
    ON courses.teacher_id = teachers.id
WHERE courses.teacher_id IS NULL;
"""
"""
SELECT
    *
FROM new_works_from_bmi_incoming AS nwifi
JOIN orders_form_stocks_exachange AS ofse
  ON nwifi.orders_id = ofse.id
WHERE ofse.total >= 1000;
"""
"""
SELECT
    *
FROM new_works_from_bmi_incoming nwifi
JOIN orders_form_stocks_exachange ofse
  ON nwifi.orders_id = ofse.id
WHERE ofse.total >= 1000;
"""

select_join_full = """
SELECT
    title, first_name, last_name, email
FROM courses
FULL JOIN teachers
    ON courses.teacher_id = teachers.id
WHERE teachers.id IS NULL OR courses.teacher_id IS NULL
"""

"""
SELECT
    u.name,
    p.name,
    o.amount
FROM orders o
JOIN users u
    ON o.user_id = u.id
JOIN products p
    ON o.product_id = p.id;
"""
'''
SELECT *
FROM users
ORDER BY
    city,
    name;
'''

select_order = """
SELECT
    title, first_name, last_name, email
FROM courses
FULL JOIN teachers
    ON courses.teacher_id = teachers.id
ORDER BY title, email
"""
"""
SELECT user_id
    FROM orders
    WHERE amount = 1200
"""
"""
SELECT *
FROM users
WHERE id in (
    SELECT DISTINCT user_id
    FROM orders
    WHERE amount = 1200
);


SELECT *
FROM users
WHERE id IN (
    SELECT user_id
    FROM orders
);


"""

check_new_data = """
SELECT
    o.id AS order_id,
    o.amount,
    o.user_id,
    p.id AS product_id,
    p.name AS product_name,
    p.price,
    p.quantity,
    u.first_name, 
    u.last_name, 
    u.email
FROM public.orders o
JOIN public.products p
    ON o.product_id = p.id
join students u
     ON u.id = o.user_id
;
"""
max_ammount = """

SELECT *
FROM orders
WHERE amount = (
    SELECT MAX(amount)
    FROM orders
);

"""

count = """
SELECT COUNT(*)
FROM orders
WHERE amount >= 300
"""
sum_avg = """
SELECT
    SUM(amount),
    AVG(amount)
FROM orders;
"""

min_max = """
SELECT
    MIN(amount),
    MAX(amount)
FROM orders;
"""

order_by_user = """
SELECT
    user_id,
    COUNT(user_id)
FROM orders
-- where  COUNT(user_id) > 2
GROUP BY user_id
HAVING COUNT(user_id) > 2
;
""" 

with get_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute(order_by_user)
        print(cursor.fetchall())
    conn.commit()


# ERROR WARNING!!!!!!
"""
SELECT *
FROM users
JOIN orders;

-- ON users.id = orders.id
++ ON users.id = orders.user_id

SELECT *
FROM orders
LIMIT 10;

"""