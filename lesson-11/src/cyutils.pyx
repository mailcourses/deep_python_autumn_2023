cpdef fibonacci(int n):
    if n < 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def hello():
    return "Hello, world"

cdef csum(int left, int right):
    cdef int res = 0
    for i in range(left, right):
        res += i
    return res
