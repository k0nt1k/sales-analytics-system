import pandas as pd
from src.database import engine


def get_customer_statistics():
    query = """
    WITH customer_orders AS (
        SELECT
            c.customer_unique_id,
            o.order_id,
            SUM(oi.price) AS order_value
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.order_status = 'delivered'
        GROUP BY c.customer_unique_id, o.order_id
    ),
    customer_summary AS (
        SELECT
            customer_unique_id,
            COUNT(*) AS total_orders,
            SUM(order_value) AS total_spent
        FROM customer_orders
        GROUP BY customer_unique_id
    )
    SELECT
        (SELECT ROUND(AVG(order_value), 2)
         FROM customer_orders) AS average_order_value,

        ROUND(AVG(total_spent), 2) AS average_customer_spending,
        COUNT(*) AS total_customers,

        COUNT(*) FILTER (
            WHERE total_orders > 1
        ) AS repeat_customers,

        ROUND(
            100.0 * COUNT(*) FILTER (
                WHERE total_orders > 1
            ) / COUNT(*),
            2
        ) AS repeat_customer_percentage

    FROM customer_summary;
    """

    return pd.read_sql(query, engine)


def get_top_customers():
    query = """
    SELECT
        c.customer_unique_id,
        ROUND(SUM(oi.price), 2) AS total_spent,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY c.customer_unique_id
    ORDER BY total_spent DESC
    LIMIT 10;
    """

    return pd.read_sql(query, engine)


if __name__ == "__main__":
    print("--- Customer Analytics ---")
    print(get_customer_statistics().to_string(index=False))

    print("\n--- Top 10 Customers ---")
    print(get_top_customers().to_string(index=False))