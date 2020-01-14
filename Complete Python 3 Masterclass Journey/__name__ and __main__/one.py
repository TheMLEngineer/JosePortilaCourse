def func():
    print('function in one.py')
    
print("Top Level print statement in one.py")

if __name__ == '__main__':
    print('one.py is run directly')
    
else:
    print('one.py is called in another module')