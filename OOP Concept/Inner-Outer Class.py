def outer():
    print(' outer function is called')

    def inner():
        print('Inner function is called')

    inner()

outer()
#inner()= Name error [never call inner function here]

# In python if function is cre4ated within another function referred to as inner function
