"""
Python functions always return a value.  Even if you explicitly 
don't return a value, the function will return None
"""

def function():
    if False:
        return True


def main():
    print "Calling function"
    if not function():
        print "Made it here because the function will always return None"


if __name__ == '__main__':
    main()

