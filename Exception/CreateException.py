def Salary(salary):
    try:
        if (salary < 0):
            raise Exception('salary cannot less than 0')
        print('salary: ', salary)
    except Exception as e:
        print('cannot read salary due to: ', e)
    else:
        print('Complete!!!')

Salary(-25000)