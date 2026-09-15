from db_connetor import get_connection

"""
CREATE TABLE users (
    id SERIAL PRIMARY KEY,                          -- Auto-increment ID
    username VARCHAR(100) NOT NULL UNIQUE,          -- Not null + unique
    email VARCHAR(100) NOT NULL UNIQUE,             -- Email унікальний
    password_hash VARCHAR(255) NOT NULL,            -- Обов'язкове поле
    first_name VARCHAR(100),                        -- Опціональне
    last_name VARCHAR(100),                         -- Опціональне
    birth_date DATE,                                -- Дата народження
    is_active BOOLEAN DEFAULT TRUE,                 -- За замовчуванням TRUE
    balance DECIMAL(10, 2) DEFAULT 0.00,            -- Грошь, 10 цифр (2 після коми)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Дата створення
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Дата оновлення
);
"""

create_products = """
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),  -- Ціна повинна бути > 0
    quantity INTEGER NOT NULL CHECK (quantity >= 0),  -- Кількість не від'ємна
    status VARCHAR(20) CHECK (status IN ('active', 'discontinued', 'pending'))
);
"""

add = """
ALTER TABLE students
ADD COLUMN phone VARCHAR(20);
"""
"""
ALTER TABLE users
ADD COLUMN phone VARCHAR(20) UNIQUE,
ADD COLUMN address TEXT;
"""
delete = """
ALTER TABLE students
DROP COLUMN phone;
"""

insert = """
INSERT INTO students
(first_name,last_name,email,phone )
VALUES ('aaaa', 'bbbb', 'ab@gmail.com', '0871112233')
"""
"""
INSERT INTO users (username, email, password_hash, is_active)
VALUES 
    ('alice_wonderland', 'alice@example.com', 'hash_alice', TRUE),
    ('bob_builder', 'bob@example.com', 'hash_bob', TRUE),
    ('charlie_brown', 'charlie@example.com', 'hash_charlie', FALSE);
"""
"""
INSERT INTO users_backup
SELECT * FROM users WHERE is_active = TRUE;
"""

wrong_insert = """
INSERT INTO products
(name, price, quantity, status)
VALUES 
('alice_wonderland', 5000, 1, 'active')
"""

update = """
UPDATE students
SET phone = '03758889911'
WHERE id = 1
"""

"""
DROP TABLE IF EXISTS users CASCADE;
"""
"""
-- Видалити всі рядки, але таблиця залишається
TRUNCATE TABLE users;
"""

#update
"""
UPDATE users
SET is_active = FALSE, updated_at = CURRENT_TIMESTAMP
WHERE updated_at < CURRENT_TIMESTAMP - INTERVAL '30 days';
"""

"""
UPDATE posts
SET author_name = users.username
FROM users
WHERE posts.user_id = users.id;
"""

select_1 ="""
SELECT * FROM students;
"""

select_2 ="""
SELECT id, email FROM students;
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

select_5 ="""
SELECT * FROM students WHERE id IN (1, 2, 3, 5)
ORDER BY last_name;
"""

with get_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute(select_5)
        print(cursor.fetchall())
    conn.commit()
