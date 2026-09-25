DROP TABLE IF EXISTS temp_orders;
DROP TABLE IF EXISTS temp_employees;

-- Таблиця працівників компанії
CREATE TEMP TABLE temp_employees (
    id          INTEGER PRIMARY KEY,
    full_name   VARCHAR(100) NOT NULL,
    position    VARCHAR(100) NOT NULL,
    is_active   BOOLEAN NOT NULL DEFAULT TRUE
);

-- Таблиця замовлень
CREATE TEMP TABLE temp_orders (
    id              INTEGER PRIMARY KEY,
    order_number    VARCHAR(30) NOT NULL UNIQUE,
    customer_name   VARCHAR(100) NOT NULL,
    total_amount    NUMERIC(10, 2) NOT NULL CHECK (total_amount >= 0),
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- Працівник, який створив / згенерував замовлення
    employee_id     INTEGER REFERENCES temp_employees(id)
);

INSERT INTO temp_employees (id, full_name, position, is_active)
VALUES
    (1, 'Анна Коваль',     'Менеджер з продажу', TRUE),
    (2, 'Богдан Петренко', 'Менеджер з продажу', TRUE),
    (3, 'Ірина Мельник',   'Оператор',           TRUE),
    (4, 'Олег Савчук',     'Менеджер з продажу', FALSE),
    (5, 'Марія Шевченко',  'Оператор',           TRUE),
    (6, 'Андрій Коваль',   'Менеджер з продажу', TRUE);

INSERT INTO temp_orders (id, order_number, customer_name, total_amount, employee_id)
VALUES
    (1, 'ORD-1001', 'ТОВ Альфа',       15000.00, 1),
    (2, 'ORD-1002', 'ПП Бета',          7800.00, 1),
    (3, 'ORD-1003', 'ТОВ Гамма',       22000.00, 2),
    (4, 'ORD-1004', 'ФОП Дельта',       4300.00, 5),
    (5, 'ORD-1005', 'ТОВ Епсілон',     12500.00, 5);

--пошук працівників, які не зробили ні одного замовлення
SELECT e.id, e.full_name, e.position, e.is_active
FROM temp_employees AS e
LEFT JOIN temp_orders AS o ON o.employee_id = e.id
WHERE o.id IS NULL
ORDER BY e.id;

DROP TABLE temp_orders;
DROP TABLE temp_employees;