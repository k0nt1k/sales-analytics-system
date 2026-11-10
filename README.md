# Sales Analytics System

A data analytics project built with Python, SQL, and PostgreSQL using real Brazilian e-commerce data from Olist.

The project analyzes sales performance, product categories, and customer purchasing behavior.

## Features

- Monthly revenue and order analysis
- Top 10 product categories by revenue
- Average order value
- Average customer spending
- Repeat customer analysis
- Top 10 customers by spending
- Data visualization using Matplotlib

## Technologies

- Python
- PostgreSQL
- SQL
- Pandas
- Matplotlib
- SQLAlchemy

## Project Structure

```text
sales-analytics-system/
│
├── data/                 # Dataset CSV files (not included in Git)
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
│
├── src/
│   ├── database.py
│   ├── sales_analysis.py
│   ├── customer_analysis.py
│   └── visualizations.py
│
├── .env                  # Database connection settings
├── .gitignore
├── requirements.txt
├── main.py
└── README.md
```

## Dataset

The project uses the [Olist Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

The dataset contains approximately 100,000 orders from 2016 to 2018.

## Setup

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd sales-analytics-system
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Download the dataset from Kaggle and place the CSV files in the `data/` folder.

5. Create a PostgreSQL database named `sales_analytics`.

6. Create the database tables using `sql/create_tables.sql` and import the CSV files into the corresponding tables. Import parent tables before dependent tables:
   - customers
   - products
   - category_translation
   - orders
   - order_items

7. Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/sales_analytics
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

## Run the Project

Run the following command from the project root:

```bash
python main.py
```

The script runs the SQL analyses, displays the results, and generates charts.

## Notes

- Revenue calculations include delivered orders only.
- Revenue is calculated from product prices (`price`) and excludes shipping costs (`freight_value`).
- Monetary values are in Brazilian reais (BRL).
- The `.env` file and dataset files are not included in the repository.