
# OOP-Inventory-System

A simple Python-based inventory management system that enables users to manage stock for various product types—Tech, Food, and Outfit. The system stores data persistently in a JSON file (stock_data.json) and supports operations like adding, deleting, selling, and restocking items.


## Features

*Item Categories:*

- Tech: Includes brand and warranty
- Food: Includes expiry date
- Outfit: Includes size and fabric

*Core Functionalities:*

- Add new items with type-specific details
- Delete items by ID
- Search items by name or category
- List all available inventory
- Sell or restock items
- Calculate total inventory value
- Remove expired food items
- Auto-save and load inventory from a JSON file

 ## File Structure

- Item (ABC): Abstract base class with common attributes and methods

- Tech, Food, Outfit: Subclasses with specialized properties and logic

- Store: Manages all item collections and inventory operations

- main(): Provides a console-based user interface to interact with the system

## Data Persistence

- Inventory data is stored in stock_data.json

- Automatically loads saved data when the program starts

## Usage

To run the system, use the following command in your terminal:

```cmd
python inventory_system.py
```
Then, simply follow the on-screen menu to manage your inventory with ease!


