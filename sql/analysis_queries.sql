-- Total number of orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- Orders by status
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;



-------------------------
SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp)::date AS month,
    ROUND(SUM(oi.price), 2) AS revenue,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY DATE_TRUNC('month', o.order_purchase_timestamp)
ORDER BY month;
-------------------------
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
-------------------------
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
    COUNT(*) FILTER (WHERE total_orders > 1) AS repeat_customers,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE total_orders > 1) / COUNT(*),
        2
    ) AS repeat_customer_percentage
FROM customer_summary;
--------------------------
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