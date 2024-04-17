price = 1000
discount = 0

if price >= 1000:
    discount = 0.15
    print('Discount: ', price * discount, 'baht')
elif price >= 500:
    discount = 0.05
    print('Discount: ', price * discount, 'baht')
else:
    print('No discount')