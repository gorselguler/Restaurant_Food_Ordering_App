Restaurant Food Ordering Application
A Python GUI application for restaurant food ordering with Tkinter.
Features

Browse Menu - View all available items with prices
Shopping Cart - Add, remove, and modify item quantities
Order Management - Complete checkout process
Order History - View all past orders
Persistent Storage - Orders saved to orders.txt file

Requirements

Python 3.x
tkinter (included with Python)

Installation

Make sure Python is installed on your system
Save the code as restaurant_app.py
Run the application:

bashpython restaurant_app.py
Usage

Add Items: Click "Add" button next to menu items
Modify Cart: Use +/- buttons to adjust quantities, X to remove items
Checkout: Click "CHECKOUT" button to place order
View History: Click "Order History" button in header
Clear Cart: Use "Clear Cart" button to empty shopping cart

Menu Items

Burger - $8.99
Pizza - $12.99
Pasta - $10.99
Salad - $6.99
Fries - $3.99
Soda - $1.99
Coffee - $2.49
Ice Cream - $4.99
Sandwich - $7.49
Soup - $5.99

Order Storage
All orders are automatically saved to orders.txt in the same directory with:

Order number
Date and time
Items and quantities
Total amount

Interface

Left Panel: Menu with all available items
Right Panel: Shopping cart with item management
Header: Order history access
Bottom: Total amount and checkout buttons
