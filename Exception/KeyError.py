try:
    data = {
        1: 'VB',
        2: 'C#'
    }
    print(data[3])
except KeyError:
    print('exception KeyError')