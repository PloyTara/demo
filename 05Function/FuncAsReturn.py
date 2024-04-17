# Function as return value

def Calculator(operation):
    def Add(x, y): return x + y
    def Sub(x, y): return x - y
    def InvalidProcess(x, y): return 0

    if operation == '+':
        return Add
    elif operation == '-':
        return Sub
    else:
        return InvalidProcess

ops = Calculator('+')
result = ops(300, 500)
print(result)