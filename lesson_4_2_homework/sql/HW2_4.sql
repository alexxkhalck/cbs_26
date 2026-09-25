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

--знайти працівників, які або працюють у IT, або мають зарплату 55 000
SELECT id, full_name, salary FROM temp_employees WHERE department = 'IT'
UNION
SELECT id, full_name, salary FROM temp_employees WHERE salary = 55000;

--знайти працівників, які одночасно працюють у IT і мають зарплату 55 000
SELECT id, full_name, salary FROM temp_employees WHERE department = 'IT'
INTERSECT
SELECT id, full_name, salary FROM temp_employees WHERE salary = 55000;

--знайдемо IT-працівників, які не мають зарплату 55 000
SELECT id, full_name, salary FROM temp_employees WHERE department = 'IT'
EXCEPT
SELECT id, full_name, salary FROM temp_employees WHERE salary = 55000;

DROP TABLE temp_employees;
--select ||/ 125