import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Basic setup
n_customers = 10000  # Increase to simulate more customers
customer_ids = [f"CUST_{i:05d}" for i in range(n_customers)]
regions = np.random.choice(['North', 'South', 'East', 'West'], size=n_customers)
genders = np.random.choice(['Male', 'Female', 'Other'], size=n_customers)
ages = np.random.randint(18, 70, size=n_customers)
signup_dates = pd.to_datetime('2020-01-01') + pd.to_timedelta(np.random.randint(0, 730, size=n_customers), unit='D')
customer_segments = np.random.choice(['Loyal', 'New', 'Occasional', 'Churned'], size=n_customers)

# Create customer dataframe
df_customers = pd.DataFrame({
    'CustomerID': customer_ids,
    'Region': regions,
    'Gender': genders,
    'Age': ages,
    'Signup_Date': signup_dates,
    'Customer_Segment': customer_segments
})

# Simulate transactions
transactions = []
payment_methods = ['Credit Card', 'Debit Card', 'UPI', 'Wallet', 'Cash']
channels = ['Mobile App', 'Website', 'In-store']
product_categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Beauty', 'Fitness', 'Groceries']

for cust_id in customer_ids:
    n_txns = np.random.poisson(15) + 1  # Ensure at least 1 transaction per customer
    txn_dates = pd.to_datetime('2023-12-31') - pd.to_timedelta(np.random.randint(1, 1095, size=n_txns), unit='D')
    for date in txn_dates:
        price = np.random.uniform(10, 500)
        discount = np.random.uniform(0, 0.4)
        quantity = np.random.randint(1, 5)
        total_price = price * quantity * (1 - discount)
        transactions.append({
            'CustomerID': cust_id,
            'Transaction_ID': f"TXN_{np.random.randint(100000, 999999)}",
            'Transaction_Date': date,
            'Quantity': quantity,
            'UnitPrice': round(price, 2),
            'Discount_pct': round(discount, 2),
            'TotalPrice': round(total_price, 2),
            'Online_Spend': round(np.random.uniform(0, total_price), 2),
            'Offline_Spend': round(np.random.uniform(0, total_price), 2),
            'Payment_Method': np.random.choice(payment_methods),
            'Channel': np.random.choice(channels),
            'Coupon_Code': np.random.choice(['NONE', 'WELCOME10', 'SAVE20', 'LOYALTY', 'FESTIVE']),
            'Product_Category': np.random.choice(product_categories),
            'Product_ID': f"PROD_{np.random.randint(1000, 9999)}",
            'Returned': np.random.choice([0, 1], p=[0.95, 0.05]),
            'Transaction_Hour': np.random.randint(0, 24),
            'Is_Holiday_Season': np.random.choice([0, 1], p=[0.85, 0.15]),
            'Month': date.month,
            'DayOfWeek': date.dayofweek
        })

# Convert to DataFrame
df_transactions = pd.DataFrame(transactions)

# Merge with customer information
df_full = df_transactions.merge(df_customers, on='CustomerID', how='left')

# Display first few rows of the generated dataset
df_full.head()

# Optionally, save to CSV
df_full.to_csv("synthetic_customer_transactions.csv", index=False)
