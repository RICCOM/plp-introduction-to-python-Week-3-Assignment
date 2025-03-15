# Define the calculate_discount function
def calculate_discount(price, discount_percent):
    """
    Calculate final price after applying discount if 20% or higher.
    
    Args:
        price (float): Original price of the item
        discount_percent (float): Discount percentage
        
    Returns:
        float: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate and display the result
final_price = calculate_discount(original_price, discount)

# Print appropriate message based on whether discount was applied
if discount >= 20:
    print(f"Original price: ${original_price:.2f}")
    print(f"Discount applied ({discount}%): Final price is ${final_price:.2f}")
else:
    print(f"No discount applied (less than 20%): Price remains ${final_price:.2f}")