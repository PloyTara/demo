##Basic Python Code##
##Discount##

def discountCal(rate, price):
    discount = rate * price
    total = price - discount
    return discount, total

while(1):
    
    price = 0
    price = float(input('ราคาสินค้า: '))

    rate = 0
    discount = 0
    total = 0

    if price >= 1000:
        rate = 0.15
        discount, total = discountCal(rate, price)
        print('ส่วนลด: ', '{:,.2f}'.format(discount), 'บาท')
        print('ราคาที่ต้องจ่าย: ', '{:,.2f}'.format(total), 'บาท')
    elif price >= 500:
        rate = 0.05
        discount, total = discountCal(rate, price)
        print('ส่วนลด: ', '{:,.2f}'.format(discount), 'บาท')
        print('ราคาที่ต้องจ่าย: ', '{:,.2f}'.format(total), 'บาท')
    else:
       print('ไม่มีส่วนลด')
       print('ราคาที่ต้องจ่าย: ', '{:,.2f}'.format(price), 'บาท') 

        

