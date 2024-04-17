##Basic Python Code##
##VAT Calculation##

price = float(input('ราคาสินค้า: '))
vat = (7/100) * price
total = price + vat
print('ราคาสินค้าก่อนรวม VAT: ', '{:,.2f}'.format(price), 'บาท')
print('VAT: ', '{:,.2f}'.format(vat), 'บาท')
print('ราคาสุทธิ: ', '{:,.2f}'.format(total), 'บาท')