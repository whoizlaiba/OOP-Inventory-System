# OOP-Inventory-System
A simple Python-based inventory management system that allows users to manage stock for different product types—Tech, Food, and Outfit. Data is persistently stored in a JSON file (stock_data.json), supporting actions like adding, deleting, selling, and restocking items.

Features

Item Categories:

Tech: Includes brand and warranty.

Food: Includes expiry date.

Outfit: Includes size and fabric.


Core Functionalities:

Add new items with type-specific details.

Delete items by ID.

Search items by name or category.

List all available inventory.

Sell or restock items.

Calculate total inventory value.

Remove expired food items.

Auto-save and load inventory from JSON file.



File Structure

Item (ABC): Abstract base class for items with common attributes and methods.

Tech, Food, Outfit: Subclasses with specific attributes and behaviors.

Store: Manages a collection of items and supports all inventory operations.

main(): Console-based user interface to interact with the system.


Data Persistence

Items are saved in a file called stock_data.json.

Automatically loads existing inventory on startup.


Usage

Run the script with Python:

python inventory_system.py

Follow the on-screen menu to manage inventory easily.



