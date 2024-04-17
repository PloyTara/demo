#Optional Parameter

def Salary(salary, ot = None):
    if ot is None:
        ot = 0
    
    otperhour = salary / 30 / 8
    return salary + (otperhour * ot)

# salary: thb
# ot: hour
result = Salary(30000, 3)
print('Total Income: ', result)