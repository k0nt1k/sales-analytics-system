from src.sales_analysis import get_monthly_sales, get_top_categories
from src.customer_analysis import get_customer_statistics, get_top_customers

from src.visualizations import (
    plot_monthly_revenue,
    plot_monthly_orders,
    plot_top_categories,
    plot_top_customers
)


def main():
    print("===== SALES ANALYTICS SYSTEM =====")

    # Sales Analysis
    print("\n--- Monthly Sales ---")
    monthly_sales = get_monthly_sales()
    print(monthly_sales.to_string(index=False))

    print("\n--- Top 10 Categories ---")
    categories = get_top_categories()
    print(categories.to_string(index=False))

    # Customer Analysis
    print("\n--- Customer Analytics ---")
    customer_stats = get_customer_statistics()
    print(customer_stats.to_string(index=False))

    print("\n--- Top 10 Customers ---")
    top_customers = get_top_customers()
    print(top_customers.to_string(index=False))

    # Visualizations
    print("\nGenerating charts...")

    plot_monthly_revenue(monthly_sales)
    plot_monthly_orders(monthly_sales)
    plot_top_categories(categories)
    plot_top_customers(top_customers)


if __name__ == "__main__":
    main()