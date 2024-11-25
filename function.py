#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
#Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price

price = float(input("Enter the price:"))
discount_percent = int(input("Enter the percentage: "))

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_percent = discount_percent / 100 
        discount = discount_percent * price
        new_price = price - discount
        print(f"The New discount is {discount_percent}, and your new price is #{new_price}, Thanks for shopping with us.")

    else:
            print(f"The percent {discount_percent}% is too low, the {price} remains the original price. Thanks for shopping with us.")
        
calculate_discount(price, discount_percent)