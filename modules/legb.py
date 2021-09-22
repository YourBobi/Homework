a = "I am global variable!"

def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        # nonlocal a для task 5.4(3)
        global a   # task 5.4(2)
        print(a)
    inner_function()    # task 5.4(1)
