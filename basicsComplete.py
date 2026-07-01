# ==========================================
# 1. VARIABLES, DATA TYPES & BASIC MATH
# ==========================================
# Python automatically detects data types
user_name = "Alex"  # String (str)
user_age = 28  # Integer (int)
wallet_balance = 150.75  # Floating point (float)
is_subscriber = True  # Boolean (bool)

# Math operations
addition = 10 + 5  # 15
subtraction = 20 - 7  # 13
multiplication = 4 * 3  # 12
division = 15 / 4  # 3.75
floor_division = 15 // 4  # 3 (drops remainder)
modulus = 15 % 4  # 3 (returns only the remainder)
exponent = 2 ** 3  # 8 (2 cubed)


# ==========================================
# 2. STRING MANIPULATION & FORMATTING
# ==========================================
# Combine strings with variables using F-strings
profile_summary = (
    f"User {user_name} is {user_age} years old with ${wallet_balance}."
)

# Useful string methods
loud_name = user_name.upper()  # "ALEX"
text_length = len(profile_summary)  # Characters count


# ==========================================
# 3. DATA STRUCTURES (COLLECTIONS)
# ==========================================
# Lists: Ordered, changeable sequences
shopping_list = ["apples", "bread", "milk"]
shopping_list.append("eggs")  # Add item
shopping_list.remove("bread")  # Remove item
first_item = shopping_list[0]  # "apples" (0-indexed)

# Dictionaries: Key-value pair storage
server_config = {
    "host": "localhost",
    "port": 8080,
    "secure": False,
}
server_config["port"] = 9000  # Update value
server_config["timeout"] = 30  # Add new pair


# ==========================================
# 4. CONDITIONAL LOGIC (IF/ELIF/ELSE)
# ==========================================
# Code executes based on matching boolean conditions
if wallet_balance > 500:
    account_status = "Premium Tier"
elif wallet_balance >= 100:
    account_status = "Standard Tier"
else:
    account_status = "Basic Tier"


# ==========================================
# 5. LOOPS (REPEATING ACTIONS)
# ==========================================
# For Loop: Iterating through a fixed list
processed_items = []
for item in shopping_list:
    processed_items.append(item.upper())

# Range Loop: Running code a specific number of times
loop_sum = 0
for i in range(1, 5):  # Numbers 1, 2, 3, 4
    loop_sum += i

# While Loop: Keeps going as long as the condition remains True
counter = 3
while counter > 0:
    counter -= 1  # Decrement to prevent infinite loop


# ==========================================
# 6. FUNCTIONS & SCOPE
# ==========================================
# Reusable code block with arguments and a return value
def calculate_tax(amount, tax_rate=0.05):
    """Calculates standard item tax."""
    total_tax = amount * tax_rate
    return round(total_tax, 2)


final_tax = calculate_tax(wallet_balance)


# ==========================================
# 7. EXECUTION / OUTPUT CHECK
# ==========================================
# Print statement to verify variables created above work correctly
print("--- PYTHON BASICS EXECUTION RUN ---")
print(profile_summary)
print(f"Account Tier determined: {account_status}")
print(f"Processed Shopping List: {processed_items}")
print(f"Calculated Tax on wallet balance: ${final_tax}")
print("-----------------------------------")
