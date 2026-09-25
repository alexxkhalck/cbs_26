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

INSERT INTO temp_employees (
    id,
    full_name,
    department,
    salary,
    age,
    email,
    is_active
)
VALUES
    (1, 'Анна Коваль',      'IT',        55000.00, 24, 'anna@example.com',  TRUE),
    (2, 'Богдан Петренко',  'Sales',     42000.00, 31, 'bohdan@example.com', TRUE),
    (3, 'Ірина Мельник',    'HR',        38000.00, 28, NULL,                FALSE),
    (4, 'Олег Савчук',      'IT',        70000.00, 35, 'oleg@example.com',  TRUE),
    (5, 'Марія Шевченко',   'Marketing', 45000.00, 26, 'maria@example.com', TRUE),
    (6, 'ivan Bondar',      NULL,        NULL,     22, 'ivan@example.com',  TRUE),
    (7, 'Андрій Коваль',    'IT',        55000.00, 30, NULL,                FALSE);

SELECT * FROM temp_employees WHERE department = 'IT';

SELECT * FROM temp_employees WHERE department <> 'IT';

SELECT full_name, age FROM temp_employees WHERE age < 30;

SELECT full_name, salary FROM temp_employees WHERE salary > 50000;

SELECT full_name, salary FROM temp_employees WHERE salary BETWEEN 40000 AND 55000;

SELECT full_name, salary FROM temp_employees WHERE salary >= 40000   AND salary <= 55000;

SELECT full_name, age FROM temp_employees WHERE age BETWEEN 25 AND 30;

SELECT full_name, department FROM temp_employees WHERE department IN ('IT', 'HR', 'Marketing');

SELECT full_name, department FROM temp_employees WHERE department = 'IT'    OR department = 'HR'
   OR department = 'Marketing';

SELECT full_name, id FROM temp_employees WHERE id IN (1, 3, 5, 7);

SELECT full_name, email FROM temp_employees WHERE email IS NULL;

SELECT * FROM temp_employees WHERE email = NULL;

SELECT full_name, department FROM temp_employees WHERE department IS DISTINCT FROM 'IT';

SELECT full_name, department FROM temp_employees WHERE department <> 'IT';

SELECT * FROM temp_employees WHERE department IS NOT DISTINCT FROM NULL;

SELECT full_name, department, salary, is_active FROM temp_employees
WHERE department = 'IT' AND salary >= 55000 AND is_active = TRUE;

SELECT full_name, department, is_active FROM temp_employees WHERE department = 'HR'
   OR is_active = FALSE;

SELECT full_name, is_active FROM temp_employees WHERE NOT is_active;

SELECT full_name, is_active FROM temp_employees WHERE is_active = FALSE;

SELECT full_name, department FROM temp_employees WHERE department NOT IN ('IT', 'HR');

SELECT full_name, department FROM temp_employees
WHERE department NOT IN ('IT', 'HR') OR department IS NULL;

SELECT full_name FROM temp_employees WHERE full_name LIKE '%Коваль%';

SELECT full_name, email FROM temp_employees WHERE email LIKE '%@example.com';

SELECT full_name FROM temp_employees WHERE full_name LIKE 'Анна ____';

SELECT full_name FROM temp_employees WHERE full_name LIKE 'ivan%';

SELECT full_name FROM temp_employees WHERE full_name ILIKE 'IVAN%';

SELECT full_name, department FROM temp_employees WHERE department ILIKE '%it%';

DROP TABLE temp_employees;
--select ||/ 125