
def main():
    usr_input = int(input(''))
    for x in in_range(usr_input): print(x, end = ' ')

def in_range(*args):
    numArgs = len(args) #Gets number of arguments
    start = 1 #Default start point
    step = 1
    if numArgs < 1 :raise TypeError(f'expected argument, got {numArgs}')
    elif numArgs == 1: stop = args[0]
    elif numArgs == 2: (start, stop) = args
    elif numArgs == 3: (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numArgs}')
    i = start
    while i <= stop:
        yield i 
        i += step

if __name__ == '__main__':main()