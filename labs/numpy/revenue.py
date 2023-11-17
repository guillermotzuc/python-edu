import numpy as np

# Item Positions: Pen, Notebook, Stapler, Backpack
north_sales = np.array([14, 12, 3, 20])
east_sales = np.array([9, 5, 23, 10])
south_sales = np.array([60, 42, 36, 90])
west_sales = np.array([23, 28, 91, 73])

sales = np.vstack([
    north_sales,
    east_sales,
    south_sales,
    west_sales,
])

prices = np.array([
  [1.5],
  [4.25],
  [6.0],
  [25.99]
])

revenues = sales @ prices
print(f"Revenues: {revenues}")
print(f"Total Revenue: {sum(revenues)}")