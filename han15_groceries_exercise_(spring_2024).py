# -*- coding: utf-8 -*-
"""han15 Groceries Exercise (Spring 2024)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18dLZNYlAEVSVAeRGSKHDKTdhFoOtkgqT

## References

  + [Lists](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/lists.md)
  + [Dictionaries](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/dictionaries.md)
  + [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html?#list-comprehensions)

# Instructions

Make a copy of this notebook so you can edit and save your own version of it. Do the work in your copy of the notebook.

The setup cell provides a Python variable called `products` and a function called `to_usd`. Remember to run the setup cells before proceeding to development.

Write Python code in the cells below to transform the provided `products` variable into the desired information outputs.

# Evaluation

Exercise submissions will be evaluated according to the rubric below:

Part | Criteria | Weight
-- | -- | --
Part 1 | Dynamically counts the number of products. | 10%
Part 1 | Loops through the products and prints the name and price of each. | 20%
Part 1 | Formats prices using provided `to_usd` function. | 10%
Part 2 | Dynamically counts the number of unique departments. | 15%
Part 2 | Loops through the departments and prints the name of each, formatted as title case. | 15%
Part 2 | Prints the number of matching products for each department. | 20%
Part 2 | Conditionally pluralizes the "product" vs "products" label depending on how many matching products there are. | 10%











This rubric is tentative, and may be subject to slight adjustments during the grading process.

# Setup
"""

#
# SETUP CELL (run and leave as-is)
#

def to_usd(my_price):
    """
        Converts a numeric value to usd-formatted string, for printing and display purposes.

        Param: my_price (int or float) like 4000.444444

        Example: to_usd(4000.444444)

        Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# example tests and invocations for the function:
assert to_usd(3.5) == "$3.50"
assert to_usd(4.44444) == "$4.44"
assert to_usd(1234567890) == "$1,234,567,890.00"
print(to_usd(12345.6789))

#
# SETUP CELL (run and leave as-is)
#

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


print(products)

"""# Part 1 (Products)

Write python code which references the `products` variable to reproduce the following output, representing a human-friendly list of products:

```
--------------
THERE ARE 20 PRODUCTS:
--------------
 + All-Seasons Salt ($4.99)
 + Chocolate Fudge Layer Cake ($18.50)
 + Chocolate Sandwich Cookies ($3.50)
 + Cut Russet Potatoes Steam N' Mash ($4.25)
 + Dry Nose Oil ($21.99)
 + Fresh Scent Dishwasher Cleaner ($4.99)
 + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
 + Green Chile Anytime Sauce ($7.99)
 + Light Strawberry Blueberry Yogurt ($6.50)
 + Mint Chocolate Flavored Syrup ($4.50)
 + Overnight Diapers Size 6 ($25.50)
 + Peach Mango Juice ($1.99)
 + Pizza For One Suprema Frozen Pizza ($12.50)
 + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
 + Pure Coconut Water With Orange ($3.50)
 + Rendered Duck Fat ($9.99)
 + Robust Golden Unsweetened Oolong Tea ($2.49)
 + Saline Nasal Mist ($16.00)
 + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
 + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)
 ```

"""

print("--------------\n")
print("THERE ARE 20 PRODUCTS:\n")
print("--------------\n")

for product in products:
  print(f"+ {product['name']} ({to_usd(product['price'])})\n")





"""# Part 2 (Departments)

Write python code which references the `products` variable to reproduce the following output, representing a human-friendly list of departments:

```
--------------
THERE ARE 10 DEPARTMENTS:
--------------
 + Babies (1 product)
 + Beverages (5 products)
 + Dairy Eggs (1 product)
 + Dry Goods Pasta (1 product)
 + Frozen (4 products)
 + Household (1 product)
 + Meat Seafood (1 product)
 + Pantry (2 products)
 + Personal Care (2 products)
 + Snacks (2 products)
 ```

> NOTE: there are many ways of counting the corresponding number of products for each department. Consider a counting approach, a filtering approach, or a [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) from the `collections` module.
"""

print("--------------\n")
print("THERE ARE 10 DEPARTMENTS:\n")
print("--------------\n")

dict_departments = []
list_departments = []

for product in products:
  if product['department'] not in list_departments:
    new_department = {'name': (f"{product['department']}"), 'count': 1}
    dict_departments.append(new_department)
    add_to_list = product['department']
    list_departments.append(add_to_list)
  elif product['department'] in list_departments:
    while n < len(dict_departments):
      if dict_departments[n]['name'] == product['department']:
        dict_departments[n]['count'] += 1
        n = len(dict_departments)
      else:
        n += 1

i = 0
while i < len(dict_departments):
  department_name = dict_departments[i]['name'].capitalize()
  count = dict_departments[i]['count']
  if count == 1:
    print(f"+ {department_name} ({count} product)")
    i += 1
  else:
    print(f"+ {department_name} ({count} products)")
    i += 1


