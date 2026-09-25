DROP TABLE IF EXISTS temp_employees;
DROP TABLE IF EXISTS temp_departments;

-- Працівники
CREATE TEMP TABLE temp_employees (
    id              INTEGER PRIMARY KEY,
    full_name       VARCHAR(100) NOT NULL,
    department_id   INTEGER,
    salary          NUMERIC(10, 2),
    is_active       BOOLEAN NOT NULL DEFAULT TRUE
);

-- Відділи
CREATE TEMP TABLE temp_departments (
    id              INTEGER PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL,
    city            VARCHAR(50) NOT NULL
);

INSERT INTO temp_departments (id, department_name, city)
VALUES (1, 'IT', 'Kyiv'),(2, 'Sales', 'Lviv'),(3, 'HR', 'Kyiv'),(4, 'Marketing', 'Odesa'),(5, 'Finance', 'Dnipro');

INSERT INTO temp_employees (id, full_name, department_id, salary, is_active)
VALUES (1, 'Анна Коваль',     1,    55000.00, TRUE),
    (2, 'Богдан Петренко', 2,    42000.00, TRUE),
    (3, 'Ірина Мельник',   3,    38000.00, FALSE),
    (4, 'Олег Савчук',     1,    70000.00, TRUE),
    (5, 'Марія Шевченко',  4,    45000.00, TRUE),
    (6, 'ivan Bondar',     NULL, NULL,     TRUE),
    (7, 'Андрій Коваль',   1,    55000.00, FALSE),
    (8, 'Тестовий запис',  99,   30000.00, TRUE);

--вибрати працівників, для яких існує відповідний відділ
SELECT e.id AS employee_id, e.full_name, e.salary, d.id AS department_id, d.department_name, d.city
FROM temp_employees AS e
INNER JOIN temp_departments AS d ON e.department_id = d.id
ORDER BY e.id;

--повертає всіх працівників із лівої таблиці та дані відділу, якщо відповідник знайдено
SELECT e.id AS employee_id, e.full_name, e.department_id AS employee_department_id,
	d.department_name, d.city
FROM temp_employees AS e
LEFT JOIN temp_departments AS d ON e.department_id = d.id
ORDER BY e.id;

--повертає всі відділи з правої таблиці і працівників, які до них належать
SELECT d.id AS department_id, d.department_name, d.city, e.id AS employee_id, e.full_name, e.salary
FROM temp_employees AS e
RIGHT JOIN temp_departments AS d ON e.department_id = d.id
ORDER BY d.id, e.id;

--повертає всі рядки з обох таблиць, якщо збіг є,
--якщо працівник не має відділу - дані відділу будуть NULL,
--якщо відділ не має працівників - дані працівника будуть NULL
SELECT e.id AS employee_id, e.full_name, e.department_id AS employee_department_id,
    d.id AS department_id, d.department_name, d.city
FROM temp_employees AS e
FULL OUTER JOIN temp_departments AS d ON e.department_id = d.id
ORDER BY COALESCE(d.id, e.department_id), e.id;

DROP TABLE IF EXISTS;
DROP TABLE IF EXISTS;