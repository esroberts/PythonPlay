"""
Python is a DYNAMICALLY, STRONGLY typed language.  
    
    Dynamically Typed - Python is dynamically typed because types are
        resolved at execution run time as opposed to compile timei

    Strongly Typed - Python is strongly typed because types are strongly
        enforced.  (e.g. you cannot concatenate an integer to a string without
        first casting the integer to a string)

"""

def concat_int_with_string():
    try:
        print str("123") + 4
    except Exception:
        print "An exception is thrown because str and integer types are incompatible"

if __name__ == "__main__":
    print "Calling concat_int_with_string().  Expect an exception to be thrown \n\
            and the print statement in the exception block to be printed"
    concat_int_with_string()
