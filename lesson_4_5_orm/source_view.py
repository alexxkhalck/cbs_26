from db_connetor import get_connection

make_view = """
CREATE OR REPLACE VIEW public.view_transactions
AS SELECT o.id AS order_id,
    o.amount,
    o.user_id,
    p.id AS product_id,
    p.name AS product_name,
    p.price,
    p.quantity,
    u.first_name,
    u.last_name,
    u.email,
        CASE
            WHEN o.amount >= 1000::numeric THEN 'EXPENSIVE'::text
            WHEN o.amount >= 225::numeric THEN 'MEDIUM'::text
            ELSE ''::text
        END AS amount_category
   FROM orders o
     JOIN products p ON o.product_id = p.id
     JOIN students u ON u.id = o.user_id;
"""

select_with = """
SELECT *
FROM view_transactions
where view_transactions.amount_category = 'MEDIUM'
"""

with get_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute(select_with)
        print(cursor.fetchall())
    conn.commit()
