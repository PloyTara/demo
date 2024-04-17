# Error handle by try except

print('Basic try...except')

try:
    print(data)
except:
    print('found program error')

print('--------------------')

print('Basic try...except: NameError')

try:
    print(data)
except NameError:
    print('variable not define')
except:
    print('found program error')

print('--------------------')

print('Basic try...except: finally')

try:
    print(data)
except NameError:
    print('variable not define')
except:
    print('found program error')
finally:
    print('end task')
