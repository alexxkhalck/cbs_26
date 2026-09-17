from db_connetor import get_connection

new_products = """
INSERT INTO public.products ("name", price, quantity, status)
VALUES
    ('Laptop Lenovo ThinkPad', 1250.00, 10, 'active'),
    ('Apple MacBook Air', 1499.99, 5, 'active'),
    ('Wireless Mouse Logitech', 35.50, 50, 'active'),
    ('Mechanical Keyboard', 89.99, 25, 'discontinued'),
    ('Monitor Dell 27"', 320.00, 15, 'active'),
    ('USB-C Hub', 45.00, 30, 'active'),
    ('Web Camera Logitech', 75.99, 20, 'active'),
    ('Headphones Sony', 199.99, 12, 'discontinued'),
    ('Laptop Stand', 55.00, 18, 'active'),
    ('HDMI Cable', 12.99, 100, 'active'),
    ('External SSD 1TB', 110.00, 8, 'discontinued'),
    ('Gaming Mouse', 65.50, 22, 'active'),
    ('Office Chair', 250.00, 7, 'active'),
    ('Desk Lamp', 29.99, 40, 'pending'),
    ('Power Bank', 49.99, 35, 'pending');
"""

create_order_table = """
CREATE TABLE public.orders (
    id serial4 PRIMARY KEY,
    amount numeric(10, 2) NOT NULL,
    user_id int4 NOT NULL,
    product_id int4 NOT NULL,

    CONSTRAINT orders_user_fk
        FOREIGN KEY (user_id)
        REFERENCES public.students(id),

    CONSTRAINT orders_product_fk
        FOREIGN KEY (product_id)
        REFERENCES public.products(id)
);
"""
insert_orders = """
INSERT INTO public.orders (amount, user_id, product_id)
VALUES
    (1250.00, 1, 4),
    (35.50,   2, 2),
    (89.99,   1, 4),
    (320.00,  3, 5),
    (1499.99, 4, 2),
    (45.00,   2, 6),
    (75.99,   5, 7),
    (199.99,  1, 8),
    (55.00,   3, 9),
    (12.99,   4, 10),
    (110.00,  2, 11),
    (65.50,   5, 12),
    (250.00,  1, 13),
    (29.99,   3, 14),
    (49.99,   4, 15);
"""

with get_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute(insert_orders)
        #print(cursor.fetchall())
    conn.commit()
