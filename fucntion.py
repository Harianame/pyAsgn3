def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

def main():
    # Prompting the user to enter original price and discount percentage
    original_price = float(input('Enter the original price: '))
    discount_percentage = float(input('Enter the discount percentage: '))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Printing the final price
    if final_price == original_price:
        print(f'No discount applied. Final price: ${final_price:.2f}')
    else:
        print(f'Discount applied. Final price: ${final_price:.2f}')

if __name__ == "__main__":
    main()
