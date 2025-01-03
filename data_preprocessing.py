# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
file_path = "C:\Project_Git\superstore_sales_data.csv"
data = pd.read_csv(file_path)


# Inspect dataset
print("Initial Data Info:")
print(data.info())

# Handle missing values
data['Postal Code'].fillna(0, inplace=True)  # Replace missing postal codes with 0

# Convert 'Order Date' to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'], format='%d/%m/%Y', errors='coerce')

# Handle invalid dates
default_date = pd.Timestamp('2000-01-01')  # Default date for invalid entries
data['Order Date'].fillna(default_date, inplace=True)

# Add Year and Month columns
data['Year'] = data['Order Date'].dt.year
data['Month'] = data['Order Date'].dt.month


# Create 'Profit Margin' column (assuming 'Profit' exists; replace if different)
if 'Profit' in data.columns and 'Sales' in data.columns:
    data['Profit Margin'] = data.apply(
        lambda x: (x['Profit'] / x['Sales'] * 100) if x['Sales'] > 0 else 0, axis=1
    )
else:
    print("Warning: 'Profit' or 'Sales' column not found.")

# Summarize data by Region
region_summary = data.groupby('Region')[['Sales']].sum().reset_index()

# Save cleaned dataset
cleaned_file_path = "C:\Project_Git\cleaned_superstore_sales_data.csv"
data.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to {cleaned_file_path}")


# Basic Visualization - Sales by Region
plt.figure(figsize=(10, 6))
plt.bar(region_summary['Region'], region_summary['Sales'], color='skyblue')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
