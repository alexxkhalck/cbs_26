-- Якщо ви запускаєте скрипт повторно в межах тієї самої сесії:
DROP TABLE IF EXISTS temp_employees;

-- TEMP = TEMPORARY
CREATE TEMP TABLE temp_employees (
    id          INTEGER PRIMARY KEY,
    full_name   VARCHAR(100) NOT NULL,
    department  VARCHAR(50),
    salary      NUMERIC(10, 2),
    age         INTEGER,
    email       VARCHAR(100),
    is_active   BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO temp_employees (id, full_name, department, salary, age, email, is_active)
VALUES
    (1, 'Анна Коваль',      'IT',        55000.00, 24, 'anna@example.com',  TRUE),
    (2, 'Богдан Петренко',  'Sales',     42000.00, 31, 'bohdan@example.com', TRUE),
    (3, 'Ірина Мельник',    'HR',        38000.00, 28, NULL,                FALSE),
    (4, 'Олег Савчук',      'IT',        70000.00, 35, 'oleg@example.com',  TRUE),
    (5, 'Марія Шевченко',   'Marketing', 45000.00, 26, 'maria@example.com', TRUE),
    (6, 'ivan Bondar',      NULL,        NULL,     22, 'ivan@example.com',  TRUE),
    (7, 'Андрій Коваль',    'IT',        55000.00, 30, NULL,                FALSE);

--знайти працівників, які не працюють у відділі IT
SELECT id, full_name FROM temp_employees
EXCEPT
SELECT id, full_name FROM temp_employees WHERE department = 'IT';

--знайти надлишок працівників
SELECT full_name FROM (VALUES ('Анна Коваль'), ('Анна Коваль'),
    ('Анна Коваль'), ('Олег Савчук'), ('Олег Савчук')) AS left_result(full_name)
EXCEPT ALL
SELECT full_name FROM (VALUES ('Анна Коваль'), ('Олег Савчук')) AS right_result(full_name);

DROP TABLE temp_employees;
--select ||/ 125