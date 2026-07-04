# Sales Data Analysis
# Author: Sakshi Jain
# Tools: Python, Pandas

# Sales data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile', 'Tablet'],
    'Sales': [50000, 30000, 20000, 60000, 45000, 25000],
    'Units': [10, 15, 8, 12, 20, 10],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South']
}

# Display data
print("SALES DATA")
print("-" * 50)
for i in range(len(data['Month'])):
    print(f"Month: {data['Month'][i]}")
    print(f"Product: {data['Product'][i]}")
    print(f"Sales: ₹{data['Sales'][i]}")
    print(f"Units Sold: {data['Units'][i]}")
    print(f"Region: {data['Region'][i]}")
    print("-" * 50)

# Total sales
total_sales = sum(data['Sales'])
total_units = sum(data['Units'])
print(f"\nTOTAL SALES: ₹{total_sales}")
print(f"TOTAL UNITS SOLD: {total_units}")

# Best month
max_sales = max(data['Sales'])
best_month = data['Month'][data['Sales'].index(max_sales)]
print(f"BEST PERFORMING MONTH: {best_month} (₹{max_sales})")

# Sales by product
print("\nSALES BY PRODUCT")
print("-" * 50)
products = set(data['Product'])
for product in products:
    product_sales = sum(data['Sales'][i] for i in range(len(data['Product'])) 
                       if data['Product'][i] == product)
    print(f"{product}: ₹{product_sales}")

# Sales by region
print("\nSALES BY REGION")
print("-" * 50)
regions = set(data['Region'])
for region in regions:
    region_sales = sum(data['Sales'][i] for i in range(len(data['Region'])) 
                      if data['Region'][i] == region)
    print(f"{region}: ₹{region_sales}")

print("\nAnalysis Complete!")
