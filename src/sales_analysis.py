import pandas as pd
from src.database import engine


def get_monthly_sales():
    query = """
    SELECT
        DATE_TRUNC('month', o.order_purchase_timestamp)::date AS month,
        ROUND(SUM(oi.price), 2) AS revenue,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY DATE_TRUNC('month', o.order_purchase_timestamp)
    ORDER BY month;
    """

    return pd.read_sql(query, engine)


def get_top_categories():
    query = """
    SELECT
        COALESCE(ct.product_category_name_english, 'unknown') AS category,
        ROUND(SUM(oi.price), 2) AS revenue,
        COUNT(*) AS items_sold
    FROM order_items oi
    JOIN orders o ON oi.order_id = o.order_id
    JOIN products p ON oi.product_id = p.product_id
    LEFT JOIN category_translation ct
        ON p.product_category_name = ct.product_category_name
    WHERE o.order_status = 'delivered'
    GROUP BY category
    ORDER BY revenue DESC
    LIMIT 10;
    """

    return pd.read_sql(query, engine)


if __name__ == "__main__":
    print(get_monthly_sales().head())
    print(get_top_categories())