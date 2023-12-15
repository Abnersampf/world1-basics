price = float(input('Enter the price of the product(R$): '))
newPrice = price - (price * 0.05)
print(f'The price of the product with 5% of discount, will be R${newPrice:.2f}')