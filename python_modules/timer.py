from time import process_time as pt

#has 4 keyword parameters
    #pre  - function to be called before timing
    #func - timed function
    #post - called after timing
    #n    - number of execution for averaging time

def timer(pre = None, func = None, post = None, n = 1):
    suma, t = 0.0, 0
    a = lambda x: (lambda: _) if x is None else x
    pre, func, post = a(pre), a(func), a(post)
    for _ in range(n):
        pre()
        temp = pt()
        func()
        suma += pt() - temp
        post()
    return suma/n

