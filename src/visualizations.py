import matplotlib.pyplot as plt


def plot_monthly_revenue(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["month"], df["revenue"], marker="o")

    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def plot_monthly_orders(df):
    plt.figure(figsize=(10, 5))
    plt.bar(df["month"].astype(str), df["total_orders"])

    plt.title("Monthly Orders")
    plt.xlabel("Month")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def plot_top_categories(df):
    plt.figure(figsize=(10, 6))
    plt.barh(df["category"], df["revenue"])

    plt.title("Top 10 Categories by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Category")

    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


def plot_top_customers(df):
    plt.figure(figsize=(10, 6))
    plt.barh(
        df["customer_unique_id"].astype(str),
        df["total_spent"]
    )

    plt.title("Top 10 Customers by Spending")
    plt.xlabel("Total Spending")
    plt.ylabel("Customer ID")

    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    from src.sales_analysis import get_monthly_sales, get_top_categories
    from src.customer_analysis import get_top_customers

    plot_monthly_revenue(get_monthly_sales())
    plot_monthly_orders(get_monthly_sales())
    plot_top_categories(get_top_categories())
    plot_top_customers(get_top_customers())