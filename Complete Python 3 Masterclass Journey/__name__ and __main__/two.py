import one

one.func()

print("Top Level print statement in two.py")

if __name__ == '__main__':
    print('two.py is run directly')
    
else:
    print('two.py is called in another module')