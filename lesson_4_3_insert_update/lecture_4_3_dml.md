# Заняття 33. DML (INSERT/UPDATE/DELETE)

**Тривалість:** 2 години (практика)

**Викладач:** Олександр Панченко / QALight  
**Курс:** Програмування Python · Модуль 5. PostgreSQL

## Цілі заняття

1. Опанувати SQL-команди для маніпуляції даними: `INSERT`, `UPDATE`, `DELETE`
2. Розуміти `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`
3. Вивчити гнучкий пошук за допомогою `LIKE` та регулярних виразів
4. Навчитися додавати та видаляти індекси для оптимізації
5. Работать з автоінкрементом та послідовностями
6. Практично застосувати все вивчене у своєму проєкті

## Частина 1. DDL — Data Definition Language

### 1.1. CREATE TABLE (Подробиця)

**CREATE TABLE** — команда для створення нової таблиці.

#### Базовий синтаксис:

```sql
CREATE TABLE table_name (
    column_name1 data_type constraints,
    column_name2 data_type constraints,
    ...
    PRIMARY KEY (column_name),
    FOREIGN KEY (column_name) REFERENCES other_table(id)
);
```

#### Повний приклад із всіма обмеженнями:

```sql
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
```

#### Обмеження (Constraints):

| Обмеження | Опис | Приклад |
|-----------|------|---------|
| `NOT NULL` | Обов'язкове значення | `name VARCHAR(100) NOT NULL` |
| `UNIQUE` | Унікальне значення | `email VARCHAR(100) UNIQUE` |
| `PRIMARY KEY` | Первинний ключ (унікальний + not null) | `id INTEGER PRIMARY KEY` |
| `FOREIGN KEY` | Зовнішній ключ | `user_id INTEGER REFERENCES users(id)` |
| `CHECK` | Перевірка значення | `age INTEGER CHECK (age >= 0)` |
| `DEFAULT` | Значення за замовчуванням | `status VARCHAR(50) DEFAULT 'active'` |

#### Приклад з CHECK:

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),  -- Ціна повинна бути > 0
    quantity INTEGER NOT NULL CHECK (quantity >= 0),  -- Кількість не від'ємна
    status VARCHAR(20) CHECK (status IN ('active', 'discontinued', 'pending'))
);
```

### 1.2. ALTER TABLE — Зміна структури таблиці

**ALTER TABLE** — команда для модифікації існуючої таблиці.

#### Додати новий стовпець:

```sql
ALTER TABLE users
ADD COLUMN phone VARCHAR(20);
```

#### Додати стовпець з обмеженнями:

```sql
ALTER TABLE users
ADD COLUMN phone VARCHAR(20) UNIQUE,
ADD COLUMN address TEXT;
```

#### Видалити стовпець:

```sql
ALTER TABLE users
DROP COLUMN phone;
```

#### Змінити тип даних стовпця:

```sql
-- Змінити VARCHAR(100) на VARCHAR(200)
ALTER TABLE users
ALTER COLUMN username TYPE VARCHAR(200);
```

#### Додати обмеження:

```sql
-- Додати NOT NULL до існуючого стовпця
ALTER TABLE users
ALTER COLUMN email SET NOT NULL;

-- Додати значення за замовчуванням
ALTER TABLE users
ALTER COLUMN is_active SET DEFAULT true;
```

#### Видалити обмеження:

```sql
-- Видалити DEFAULT
ALTER TABLE users
ALTER COLUMN is_active DROP DEFAULT;
```

#### Видалити первинний ключ:

```sql
ALTER TABLE users
DROP CONSTRAINT users_pkey;  -- Назва залежить від БД
```

#### Додати обмеження UNIQUE:

```sql
ALTER TABLE users
ADD CONSTRAINT unique_email UNIQUE (email);
```

### 1.3. DROP TABLE — Видалення таблиці

```sql
-- Видалити таблицю (якщо існує)
DROP TABLE IF EXISTS users;

-- Видалити таблицю та всі залежні об'єкти (каскадне видалення)
DROP TABLE IF EXISTS users CASCADE;
```

#### Рівні видалення:

| Рівень | Описание | Приклад |
|--------|----------|---------|
| `DROP TABLE` | Видалити таблицю | `DROP TABLE users;` |
| `DROP TABLE IF EXISTS` | Видалити, якщо існує | `DROP TABLE IF EXISTS users;` |
| `DROP TABLE ... CASCADE` | Видалити та залежні об'єкти | `DROP TABLE users CASCADE;` |

### 1.4. TRUNCATE — Видалення всіх даних (швидко)

```sql
-- Видалити всі рядки, але таблиця залишається
TRUNCATE TABLE users;

-- TRUNCATE каскадом (видаляє також залежні дані)
TRUNCATE TABLE users CASCADE;
```

#### TRUNCATE vs DELETE:

| Параметр | TRUNCATE | DELETE |
|----------|----------|--------|
| **Швидкість** | Швидко (не логується) | Повільніше (логується) |
| **WHERE** | Не підтримує | Підтримує `WHERE` |
| **Транзакції** | Можна ROLLBACK | Можна ROLLBACK |
| **ID** | Скидає SEQUENCE | Не скидає |
| **Обмеження** | Без CASCADE — помилка | Видаляє залежні дані |

## Частина 2. DML — Data Manipulation Language

### 2.1. INSERT — Вставка даних

#### Базовий синтаксис:

```sql
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

#### Приклад 1: Вставити одного користувача

```sql
INSERT INTO users (username, email, password_hash)
VALUES ('ivan_petrov', 'ivan@example.com', 'hashed_password_123');
```

#### Приклад 2: Вставити без вказування стовпців (всі стовпці):

```sql
INSERT INTO users
VALUES (1, 'maria_sidorenko', 'maria@example.com', 'hashed_password_456', 'Maria', 'Sidorenko', NULL, TRUE, 0.00, NOW(), NOW());
```

#### Приклад 3: Вставити кілька рядків одночасно:

```sql
INSERT INTO users (username, email, password_hash, is_active)
VALUES 
    ('alice_wonderland', 'alice@example.com', 'hash_alice', TRUE),
    ('bob_builder', 'bob@example.com', 'hash_bob', TRUE),
    ('charlie_brown', 'charlie@example.com', 'hash_charlie', FALSE);
```

#### Приклад 4: Вставити з SELECT (копіювання даних):

```sql
-- Скопіювати всіх активних користувачів у backup таблицю
INSERT INTO users_backup
SELECT * FROM users WHERE is_active = TRUE;
```

#### RETURNING — повернути вставлені дані:

```sql
INSERT INTO users (username, email, password_hash)
VALUES ('new_user', 'new@example.com', 'hashed_pass')
RETURNING id, username, email;

-- Результат: повертає ID нового користувача та його дані
-- id | username | email
-- 5  | new_user | new@example.com
```

### 2.2. UPDATE — Оновлення даних

#### Базовий синтаксис:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

#### Приклад 1: Оновити користувача по ID:

```sql
UPDATE users
SET email = 'newemail@example.com', updated_at = CURRENT_TIMESTAMP
WHERE id = 1;
```

#### Приклад 2: Оновити кілька користувачів:

```sql
-- Неактивувати всіх користувачів, які не входили 30 днів
UPDATE users
SET is_active = FALSE, updated_at = CURRENT_TIMESTAMP
WHERE updated_at < CURRENT_TIMESTAMP - INTERVAL '30 days';
```

#### Приклад 3: Оновити з виразом:

```sql
-- Збільшити баланс на 10% для всіх активних користувачів
UPDATE users
SET balance = balance * 1.1, updated_at = CURRENT_TIMESTAMP
WHERE is_active = TRUE;
```

#### Приклад 4: Оновити від іншої таблиці (JOIN):

```sql
-- Оновити поле user в таблиці posts на основі users
UPDATE posts
SET author_name = users.username
FROM users
WHERE posts.user_id = users.id;
```

#### Приклад 5: RETURNING для перевірки:

```sql
UPDATE users
SET balance = balance - 100
WHERE id = 1 AND balance >= 100
RETURNING id, username, balance;
```

#### ⚠️ НЕБЕЗПЕЧНО! UPDATE без WHERE:

```sql
-- ❌ НІКОЛИ не робіть так без WHERE!
UPDATE users SET is_active = FALSE;  -- Деактивує ВСІХ користувачів!

-- ✅ ПРАВИЛЬНО з WHERE:
UPDATE users SET is_active = FALSE WHERE id = 1;
```

### 2.3. DELETE — Видалення даних

#### Базовий синтаксис:

```sql
DELETE FROM table_name
WHERE condition;
```

#### Приклад 1: Видалити користувача по ID:

```sql
DELETE FROM users WHERE id = 5;
```

#### Приклад 2: Видалити кілька записів:

```sql
-- Видалити всіх неактивних користувачів
DELETE FROM users WHERE is_active = FALSE;
```

#### Приклад 3: Видалити з умовою на дату:

```sql
-- Видалити користувачів, які не входили більше 1 року
DELETE FROM users
WHERE updated_at < CURRENT_TIMESTAMP - INTERVAL '1 year';
```

#### Приклад 4: RETURNING для перевірки:

```sql
DELETE FROM users WHERE id = 5
RETURNING id, username, email;

-- Показує, що саме було видалено
```

#### Приклад 5: Видалити з JOIN (складна умова):

```sql
-- Видалити всі давні замовлення користувача ivan_petrov
DELETE FROM orders
WHERE user_id IN (
    SELECT id FROM users WHERE username = 'ivan_petrov'
) AND created_at < CURRENT_TIMESTAMP - INTERVAL '1 year';
```

#### ⚠️ НЕБЕЗПЕЧНО! DELETE без WHERE:

```sql
-- ❌ НІКОЛИ не робіть так!
DELETE FROM users;  -- Видалить ВСІХ користувачів!

-- ✅ ПРАВИЛЬНО:
DELETE FROM users WHERE id = 1;
```

## Частина 3. DQL — Data Query Language (SELECT)

### 3.1. Базовий SELECT

```sql
-- Усі стовпці з таблиці
SELECT * FROM users;

-- Конкретні стовпці
SELECT id, username, email FROM users;

-- З псевдонімами
SELECT 
    id AS user_id,
    username AS user_name,
    email AS user_email
FROM users;
```

### 3.2. WHERE — Умови фільтрування

#### Оператори порівняння:

```sql
SELECT * FROM users WHERE id = 1;              -- Рівність
SELECT * FROM users WHERE id != 1;             -- Не рівно
SELECT * FROM users WHERE id <> 1;             -- Альтернатива для !=
SELECT * FROM users WHERE age > 18;            -- Більше
SELECT * FROM users WHERE age >= 18;           -- Більше або рівно
SELECT * FROM users WHERE age < 30;            -- Менше
SELECT * FROM users WHERE balance <= 1000;     -- Менше або рівно
```

#### Логічні оператори:

```sql
-- AND (обидва умови повинні бути TRUE)
SELECT * FROM users WHERE is_active = TRUE AND age > 18;

-- OR (одна з умов повинна бути TRUE)
SELECT * FROM users WHERE is_active = FALSE OR balance < 100;

-- NOT (заперечення)
SELECT * FROM users WHERE NOT is_active;  -- Еквівалентно is_active = FALSE
```

#### IN (перевірка належності до списку):

```sql
SELECT * FROM users WHERE id IN (1, 2, 3, 5);
SELECT * FROM users WHERE username IN ('ivan', 'maria', 'petro');
```

#### BETWEEN (діапазон значень):

```sql
SELECT * FROM users WHERE age BETWEEN 18 AND 65;
SELECT * FROM users WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
```

#### IS NULL / IS NOT NULL:

```sql
SELECT * FROM users WHERE phone IS NULL;        -- Немає телефону
SELECT * FROM users WHERE last_name IS NOT NULL;  -- Є прізвище
```

### 3.3. LIKE — Гнучкий пошук за текстом

**LIKE** — оператор для пошуку за шаблоном (pattern matching).

#### Метасимволи:

| Символ | Пояснення | Приклад |
|--------|----------|---------|
| `%` | Будь-яка кількість будь-яких символів | `'%example%'` |
| `_` | Рівно один символ | `'user_'` |

#### Приклади 1: Пошук із префіксом

```sql
-- Користувачі, чиї імена починаються на 'Ivan'
SELECT * FROM users WHERE username LIKE 'Ivan%';

-- Результати: ivan_petrov, ivan_sidorenko, IvanTheGreat
```

#### Приклади 2: Пошук із суфіксом

```sql
-- Користувачі, чиї імена закінчуються на '_petrov'
SELECT * FROM users WHERE username LIKE '%_petrov';

-- Результати: ivan_petrov, maria_petrov, alex_petrov
```

#### Приклади 3: Пошук з рядком у середині

```sql
-- Користувачі, в імені яких є 'test'
SELECT * FROM users WHERE username LIKE '%test%';

-- Результати: test_user, my_test_account, testing123
```

#### Приклади 4: Пошук з одним невідомим символом

```sql
-- Користувачі з четирьохсимвольним ім'ям вигляду 'test'
SELECT * FROM users WHERE username LIKE 'test_';

-- Результати: test1, testa, testX (але не test12)
```

#### Приклади 5: Пошук email-адреси

```sql
-- Користувачі, які мають gmail
SELECT * FROM users WHERE email LIKE '%@gmail.com';

-- Користувачі з будь-яким доменом
SELECT * FROM users WHERE email LIKE '%@%.%';
```

#### ILIKE — Case-insensitive LIKE (PostgreSQL):

```sql
-- Незалежно від регістру
SELECT * FROM users WHERE username ILIKE 'ivan%';

-- Знаходить: ivan, Ivan, IVAN, iVaN
```

#### NOT LIKE:

```sql
-- Користувачі, які НЕ мають gmail
SELECT * FROM users WHERE email NOT LIKE '%@gmail.com';
```

#### ⚠️ Екранування спеціальних символів:

```sql
-- Шукати рядок, який містить саме '%' або '_'
SELECT * FROM users WHERE username LIKE '%\%%' ESCAPE '\';
SELECT * FROM users WHERE username LIKE '%\_\_%' ESCAPE '\';
```

### 3.4. DISTINCT — Унікальні значення

```sql
-- Всі унікальні домени email-адрес
SELECT DISTINCT SUBSTRING(email FROM '@' FOR 100) AS domain FROM users;

-- Результати: @gmail.com, @yahoo.com, @company.com

-- Кількість унікальних доменів
SELECT COUNT(DISTINCT domain) FROM users;
```

### 3.5. ORDER BY — Сортування

```sql
-- За зростанням (за замовчуванням)
SELECT * FROM users ORDER BY created_at ASC;

-- За спаданням
SELECT * FROM users ORDER BY balance DESC;

-- За кількома стовпцями
SELECT * FROM users 
ORDER BY is_active DESC, created_at DESC;

-- Alfabetичне сортування (case-insensitive)
SELECT * FROM users ORDER BY LOWER(username);
```

### 3.6. LIMIT та OFFSET — Пагінація

```sql
-- Перші 10 рядків
SELECT * FROM users LIMIT 10;

-- Рядки з 21 по 30 (перейти на 20, взяти 10)
SELECT * FROM users LIMIT 10 OFFSET 20;

-- PostgreSQL синтаксис (альтернатива)
SELECT * FROM users OFFSET 20 LIMIT 10;
```

#### Приклад: Реалізація пагінації

```python
# Користувач на сторінці 3, по 10 записів на сторінку
page = 3
per_page = 10
offset = (page - 1) * per_page  # = 20

# SQL з Python
cur.execute(
    "SELECT * FROM users ORDER BY id LIMIT %s OFFSET %s;",
    (per_page, offset)
)
```

## Частина 4. Автоінкремент та SEQUENCE

### 4.1. SERIAL — Автоматичне збільшення

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,  -- Автоматично генерує 1, 2, 3, ...
    title VARCHAR(255)
);

-- При вставці — ID генерується автоматично
INSERT INTO tasks (title) VALUES ('Завдання 1');
INSERT INTO tasks (title) VALUES ('Завдання 2');

-- Результат: id 1, 2 (без явного указання)
```

#### Типи SERIAL:

| Тип | Базовий тип | Діапазон |
|-----|------------|----------|
| `SMALLSERIAL` | `SMALLINT` | 1 до 32,767 |
| `SERIAL` | `INTEGER` | 1 до 2,147,483,647 |
| `BIGSERIAL` | `BIGINT` | 1 до 9,223,372,036,854,775,807 |

### 4.2. Робота з SEQUENCE напряму

```sql
-- Перегляд поточного значення
SELECT nextval('tasks_id_seq');  -- Повертає наступне число і збільшує

-- Отримати поточне значення БЕЗ збільшення
SELECT currval('tasks_id_seq');

-- Встановити послідовність на конкретне значення
SELECT setval('tasks_id_seq', 1000);

-- Перевірити стан послідовності
SELECT last_value, increment_by FROM tasks_id_seq;
```

### 4.3. Скидання автоінкременту

```sql
-- Скинути SEQUENCE після TRUNCATE (PostgreSQL)
TRUNCATE TABLE tasks RESTART IDENTITY;

-- Скинути SEQUENCE вручну
ALTER SEQUENCE tasks_id_seq RESTART WITH 1;
```

## Частина 5. ІНДЕКСИ

### 5.1. Що таке індекс?

**Індекс** — це структура даних, яка прискорює пошук по таблиці (як предметний покажчик у книзі).

#### Переваги та недоліки:

| Аспект | Індекс | |
|--------|--------|---|
| **Пошук** | ⚡ Швидко (O(log n)) | Без індексу (O(n)) |
| **Вставка** | Повільніше (потрібно оновити індекс) | Швидше |
| **Оновлення** | Повільніше (потрібно оновити індекс) | Швидше |
| **Розмір БД** | Займає додатковий простір | Коротка |

#### Коли створювати індекс:

✅ На стовпцях, за якими часто шукати (`WHERE`)  
✅ На стовпцях, які часто з'являються у `JOIN`  
✅ На стовпцях з обмеженням `UNIQUE` або `PRIMARY KEY`  
✅ На стовпцях у `ORDER BY` та `GROUP BY`

❌ НЕ створювати на маленьких таблицях  
❌ НЕ створювати на стовпцях зі слабкою селективністю (багато однакових значень)  
❌ НЕ створювати на булівських стовпцях (мало унікальних значень)

### 5.2. Типи індексів

#### 1. B-tree (за замовчуванням)

```sql
-- Найпоширеніший тип, відмінно працює для більшості операцій
CREATE INDEX idx_users_email ON users(email);

-- Порядок сортування в індексі
CREATE INDEX idx_users_created ON users(created_at DESC);
```

#### 2. Hash

```sql
-- Швидкий для точного пошуку (=), але не для діапазонів
CREATE INDEX idx_users_email_hash ON users USING HASH (email);
```

#### 3. GIN (Generalized Inverted Index)

```sql
-- Для складних типів даних (JSON, масиви)
CREATE INDEX idx_users_metadata ON users USING GIN (metadata);
```

#### 4. GIST (Generalized Search Tree)

```sql
-- Для географічних координат, текстового пошуку
CREATE INDEX idx_users_location ON users USING GIST (location);
```

### 5.3. Створення індексів

#### Простий індекс (один стовпець):

```sql
-- Базовий синтаксис
CREATE INDEX idx_name ON table_name (column_name);

-- На стовпці email
CREATE INDEX idx_users_email ON users (email);
```

#### Складовий індекс (кілька стовпців):

```sql
-- Індекс на двох стовпцях
CREATE INDEX idx_users_active_date ON users (is_active, created_at DESC);

-- Цей індекс прискорює запити типу:
-- SELECT * FROM users WHERE is_active = TRUE ORDER BY created_at DESC;
```

#### Унікальний індекс (UNIQUE INDEX):

```sql
-- Індекс, що гарантує унікальність
CREATE UNIQUE INDEX idx_users_email_unique ON users (email);

-- Еквівалентно ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);
```

#### Часткові індекси (PARTIAL INDEX):

```sql
-- Індекс тільки на активних користувачах (економить місце)
CREATE INDEX idx_users_email_active ON users (email)
WHERE is_active = TRUE;

-- Цей індекс використовується для запитів типу:
-- SELECT * FROM users WHERE is_active = TRUE AND email = 'ivan@example.com';
```

#### Індекс з виразом (EXPRESSION):

```sql
-- Індекс на нижньому регістрі username (для case-insensitive пошуку)
CREATE INDEX idx_users_username_lower ON users (LOWER(username));

-- Тепер цей запит буде швидким:
-- SELECT * FROM users WHERE LOWER(username) = 'ivan_petrov';
```

### 5.4. Перегляд індексів

```sql
-- Всі індекси в таблиці
SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'users';

-- Результат:
-- indexname              | indexdef
-- users_pkey             | CREATE UNIQUE INDEX users_pkey ON public.users USING btree (id)
-- idx_users_email        | CREATE INDEX idx_users_email ON public.users USING btree (email)
-- idx_users_created      | CREATE INDEX idx_users_created ON public.users USING btree (created_at)
```

### 5.5. Видалення індексів

```sql
-- Видалити індекс
DROP INDEX idx_users_email;

-- Видалити, якщо існує
DROP INDEX IF EXISTS idx_users_email;

-- Видалити з каскадом (видалить залежні об'єкти)
DROP INDEX idx_users_email CASCADE;
```

### 5.6. Аналіз продуктивності індексів

```sql
-- Увімкнути показ плану виконання запиту
EXPLAIN SELECT * FROM users WHERE email = 'ivan@example.com';

-- З детальним аналізом
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'ivan@example.com';

-- Результат показує, чи використовується індекс:
-- Index Scan using idx_users_email on users  (good!)
-- Seq Scan on users                           (bad! full table scan)
```

#### Приклад виводу EXPLAIN:

```
                              QUERY PLAN
──────────────────────────────────────────────────────────
 Index Scan using idx_users_email on users (cost=0.29..8.30 rows=1)
   Index Cond: (email = 'ivan@example.com')
 Planning time: 0.045 ms
 Execution time: 0.025 ms
```

## Частина 6. Практичні приклади

### 6.1. Повний цикл CRUD з індексом

```sql
-- 1. Створити таблицю
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Створити індекси для частих операцій
CREATE INDEX idx_products_name ON products (name);
CREATE INDEX idx_products_price ON products (price);
CREATE INDEX idx_products_active_created ON products (is_active, created_at DESC)
WHERE is_active = TRUE;

-- 3. INSERT — додати продукти
INSERT INTO products (name, description, price, quantity)
VALUES 
    ('Laptop', 'High-performance laptop', 1299.99, 10),
    ('Phone', 'Smartphone', 799.99, 25),
    ('Tablet', 'Tablet device', 499.99, 15)
RETURNING id, name, price;

-- 4. SELECT — пошук з індексом
SELECT * FROM products WHERE name = 'Laptop';  -- Швидко (індекс)
SELECT * FROM products WHERE price < 1000 ORDER BY price DESC;  -- Швидко (індекс)

-- 5. UPDATE — оновити ціну
UPDATE products
SET price = 1199.99, updated_at = CURRENT_TIMESTAMP
WHERE name = 'Laptop'
RETURNING *;

-- 6. DELETE — видалити неактивні продукти
DELETE FROM products WHERE is_active = FALSE AND quantity = 0;

-- 7. Перегляд індексів
SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'products';
```

### 6.2. Пошук за LIKE з індексом

```sql
-- Таблиця користувачів
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Індекс на username для пошуку LIKE
CREATE INDEX idx_users_username ON users (username);

-- Пошук користувачів
SELECT * FROM users WHERE username LIKE 'ivan%';  -- Користувачі, які починаються на 'ivan'
SELECT * FROM users WHERE email LIKE '%@gmail.com';  -- Користувачі з gmail
SELECT * FROM users WHERE username ILIKE 'test%';  -- Case-insensitive
```

### 6.3. Сортування і LIMIT для пагінації

```sql
-- Отримати перші 10 новітніх користувачів
SELECT id, username, created_at
FROM users
ORDER BY created_at DESC
LIMIT 10;

-- Пагінація (сторінка 2, по 10 записів)
SELECT id, username, created_at
FROM users
ORDER BY created_at DESC
LIMIT 10 OFFSET 10;

-- З підрахунком загальної кількості
SELECT COUNT(*) as total FROM users;  -- Окремий запит для загальної кількості
```

### 6.4. UPDATE з виразом (списання з баланса)

```sql
-- Таблиця рахунків користувачів
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    balance DECIMAL(10, 2) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Списати 100 з рахунку користувача (за умови достатніх коштів)
UPDATE accounts
SET balance = balance - 100, updated_at = CURRENT_TIMESTAMP
WHERE user_id = 1 AND balance >= 100
RETURNING user_id, balance;

-- Перевести гроші від користувача 1 до користувача 2
UPDATE accounts
SET balance = balance - 50
WHERE user_id = 1;

UPDATE accounts
SET balance = balance + 50
WHERE user_id = 2;
```

### 6.5. DELETE з подзапитом

```sql
-- Видалити посты давніх користувачів
DELETE FROM posts
WHERE user_id IN (
    SELECT id FROM users 
    WHERE created_at < CURRENT_TIMESTAMP - INTERVAL '1 year'
);

-- Видалити коментарі до видалених постів
DELETE FROM comments
WHERE post_id IN (
    SELECT id FROM posts WHERE is_deleted = TRUE
);
```

## Частина 7. Практичні приклади з Python

### 7.1. CRUD операції через psycopg

```python
import psycopg

DSN = "postgresql://postgres:password@localhost:5432/shop"

# CREATE — додати продукт
def add_product(name: str, price: float, quantity: int):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO products (name, price, quantity) 
                   VALUES (%s, %s, %s) RETURNING id, name, price;""",
                (name, price, quantity)
            )
            product = cur.fetchone()
            conn.commit()
            return product

# READ — отримати продукт
def get_product(product_id: int):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM products WHERE id = %s;",
                (product_id,)
            )
            return cur.fetchone()

# UPDATE — оновити ціну
def update_price(product_id: int, new_price: float):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """UPDATE products 
                   SET price = %s, updated_at = CURRENT_TIMESTAMP 
                   WHERE id = %s RETURNING id, name, price;""",
                (new_price, product_id)
            )
            result = cur.fetchone()
            conn.commit()
            return result

# DELETE — видалити продукт
def delete_product(product_id: int):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM products WHERE id = %s RETURNING id, name;",
                (product_id,)
            )
            result = cur.fetchone()
            conn.commit()
            return result
```

### 7.2. Пошук з LIKE та пагінацією

```python
def search_products(search_term: str, page: int = 1, per_page: int = 10):
    """Пошук продуктів з пагінацією"""
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            # Загальна кількість результатів
            cur.execute(
                "SELECT COUNT(*) FROM products WHERE name ILIKE %s;",
                (f"%{search_term}%",)
            )
            total = cur.fetchone()[0]
            
            # Товари на сторінці
            offset = (page - 1) * per_page
            cur.execute(
                """SELECT id, name, price, quantity FROM products 
                   WHERE name ILIKE %s
                   ORDER BY created_at DESC
                   LIMIT %s OFFSET %s;""",
                (f"%{search_term}%", per_page, offset)
            )
            
            products = cur.fetchall()
            total_pages = (total + per_page - 1) // per_page
            
            return {
                "products": products,
                "total": total,
                "page": page,
                "total_pages": total_pages
            }

# Використання
result = search_products("laptop", page=1, per_page=10)
print(f"Знайдено {result['total']} товарів")
for product in result['products']:
    print(f"  - {product[1]}: ${product[2]}")
```

### 7.3. Транзакція з UPDATE та DELETE

```python
def transfer_inventory(from_product_id: int, to_product_id: int, quantity: int):
    """Перенести кількість з одного товару до іншого"""
    try:
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                # Перевірити, чи є кількість в першого товару
                cur.execute(
                    "SELECT quantity FROM products WHERE id = %s;",
                    (from_product_id,)
                )
                available = cur.fetchone()[0]
                
                if available < quantity:
                    raise ValueError(f"Недостатньо кількості. Доступно: {available}")
                
                # Зменшити кількість у першого товару
                cur.execute(
                    "UPDATE products SET quantity = quantity - %s WHERE id = %s;",
                    (quantity, from_product_id)
                )
                
                # Збільшити кількість у другого товару
                cur.execute(
                    "UPDATE products SET quantity = quantity + %s WHERE id = %s;",
                    (quantity, to_product_id)
                )
                
                conn.commit()
                return True
    
    except Exception as e:
        conn.rollback()
        print(f"Помилка: {e}")
        return False
```

### 7.4. Отримання та індексація даних

```python
def create_database_indexes():
    """Створити оптимальні індекси для часто використовуваних запитів"""
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            # Індекси на основні стовпці пошуку
            cur.execute("""
                CREATE INDEX IF NOT EXISTS idx_products_name 
                ON products(name);
            """)
            
            cur.execute("""
                CREATE INDEX IF NOT EXISTS idx_products_price 
                ON products(price);
            """)
            
            # Часткові індекси для активних товарів
            cur.execute("""
                CREATE INDEX IF NOT EXISTS idx_products_active 
                ON products(created_at DESC)
                WHERE is_active = TRUE;
            """)
            
            conn.commit()
            print("✅ Індекси створені")

def analyze_query_plan(query: str):
    """Аналізувати план виконання запиту"""
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(f"EXPLAIN ANALYZE {query};")
            plan = cur.fetchall()
            
            print("\n📊 План виконання запиту:")
            for row in plan:
                print(row[0])
```

## Частина 8. Поради щодо оптимізації

### 8.1. Правила для доброї продуктивності

1. **Завжди створюйте індекси на стовпцях у WHERE**, особливо у JOIN
2. **Використовуйте EXPLAIN ANALYZE**, щоб перевіряти, чи використовується індекс
3. **Избегайте SELECT \***— виберіть необхідні стовпці
4. **Використовуйте LIMIT**, щоб обмежити кількість результатів
5. **Групуйте запити** в транзакції для зменшення часу підключення
6. **Регулярно вакуумуйте таблиці** (VACUUM ANALYZE)

### 8.2. Типова помилка: N+1 query

#### ❌ ПОГАНО: N+1 запити

```python
# Отримати користувачів
cur.execute("SELECT id, username FROM users;")
users = cur.fetchall()

# Для кожного користувача — окремий запит для його постів (N запитів!)
for user_id, username in users:
    cur.execute("SELECT title FROM posts WHERE user_id = %s;", (user_id,))
    posts = cur.fetchall()
    print(f"{username}: {posts}")

# Якщо 100 користувачів — це 101 запит! 😱
```

#### ✅ ДОБРЕ: Один JOIN запит

```python
# Один запит замість 101
cur.execute("""
    SELECT u.username, p.title
    FROM users u
    LEFT JOIN posts p ON u.id = p.user_id
    ORDER BY u.username;
""")

for username, title in cur.fetchall():
    print(f"{username}: {title}")

# Набагато швидше! ⚡
```

## Практичні завдання

### Завдання 1: Створити та заповнити таблиці

```sql
-- Таблиця користувачів
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблиця записів
CREATE TABLE blog_posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Вставити дані
INSERT INTO users (username, email) VALUES 
('ivan', 'ivan@example.com'),
('maria', 'maria@example.com'),
('petro', 'petro@example.com');

INSERT INTO blog_posts (title, content, user_id) VALUES
('Перший пост', 'Вміст першого посту', 1),
('Другий пост', 'Вміст другого посту', 1),
('Третій пост', 'Вміст третього посту', 2);
```

### Завдання 2: Пошук за LIKE

```sql
-- Користувачі, в іменах яких є 'test'
SELECT * FROM users WHERE username LIKE '%test%';

-- Email-адреси з gmail
SELECT * FROM users WHERE email LIKE '%@gmail.com';

-- Пости, у назвах яких є 'пост' (case-insensitive)
SELECT * FROM blog_posts WHERE title ILIKE '%пост%';
```

### Завдання 3: Оновлення та видалення

```sql
-- Оновити email користувача
UPDATE users SET email = 'newemail@example.com' WHERE id = 1;

-- Видалити всі пости користувача
DELETE FROM blog_posts WHERE user_id = 3;

-- Видалити користувача (посты видаляться через CASCADE)
DELETE FROM users WHERE id = 3;
```

### Завдання 4: Індекси та оптимізація

```sql
-- Створити індекси
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_blog_posts_user_id ON blog_posts(user_id);
CREATE INDEX idx_blog_posts_created ON blog_posts(created_at DESC);

-- Перевірити план запиту
EXPLAIN ANALYZE SELECT * FROM blog_posts WHERE user_id = 1;
```

## Підсумок

На цьому занятті ми:

✅ Вивчили **DDL команди** (CREATE TABLE, ALTER TABLE, DROP TABLE)  
✅ Опанували **DML команди** (INSERT, UPDATE, DELETE)  
✅ Навчилися **пошуку LIKE** для гнучкого фільтрування  
✅ Розібралися з **SERIAL та автоінкрементом**  
✅ Впровадили **індекси** для оптимізації  
✅ Виконали **практичні приклади** через Python  
✅ Вивчили **оптимізацію запитів** та уникання помилок

## Корисні посилання

- **PostgreSQL SQL Reference:** https://www.postgresql.org/docs/current/sql.html
- **Index Types:** https://www.postgresql.org/docs/current/indexes-types.html
- **EXPLAIN:** https://www.postgresql.org/docs/current/sql-explain.html
- **SQL Tutorial:** https://www.w3schools.com/sql/

## Питання для самоперевірки

1. Яка різниця між CREATE, ALTER та DROP?
2. Коли використовувати LIKE vs `=` в WHERE?
3. Що таке індекс і як він впливає на продуктивність?
4. Як уникнути помилки N+1 запитів?
5. Яка різниця між UPDATE без WHERE та з WHERE?
6. Як перевірити, чи використовується індекс запитом?
7. Що такое SERIAL и коли його скидати?
8. Які типи індексів підтримує PostgreSQL?

**Підготовано:** Олександр Панченко  
**Дата:** 2024  
**QALight Training Center**  
**Сертифікований курс Python**
