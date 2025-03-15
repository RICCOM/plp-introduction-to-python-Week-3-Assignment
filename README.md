This Python program implements a discount calculator that applies a discount to an item's price based on a percentage, but only if the discount is 20% or higher.

## Features
- **Function**: `calculate_discount(price, discount_percent)`
  - Takes original price and discount percentage as parameters
  - Applies discount if 20% or higher
  - Returns original price if discount is less than 20%
- User input for price and discount percentage
- Formatted output showing final price or indicating no discount applied

## Requirements
- Python 3.x

## Usage
1. Run the program
2. Enter the original price when prompted
3. Enter the discount percentage when prompted
4. View the result:
   - If discount ≥ 20%: Shows original and discounted price
   - If discount < 20%: Shows original price with no discount message
