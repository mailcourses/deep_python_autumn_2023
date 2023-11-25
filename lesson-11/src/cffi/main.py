#! /usr/bin/env python3

import cffi

def main():
    ffi = cffi.FFI()
    lib = ffi.dlopen('../ctypes_lib/libutils.so')
    ffi.cdef('''
    int sum(int* arr, int n);
    int fibonacci(int n);
    ''')

    lst = list(range(0, 10))
    len_lst = len(lst)
    arr_var = ffi.new('int[]', lst);
    print(arr_var, type(arr_var))
    res = lib.sum(arr_var, len_lst)
    print(f"Sum of {lst} is {res}", sum(lst))
    res = lib.fibonacci(34)
    print(f"Fibonacci's 34th number is {res}")

    ffi.cdef('''
    struct Point
    {
        int x;
        int y;
    };

    int area(struct Point*, struct Point*);
    ''')
    p1 = ffi.new('struct Point*')
    p2 = ffi.new('struct Point*')

    p1.x, p1.y = (10, 10)
    p2.x, p2.y = (0, 5)
    res = lib.area(p1, p2)
    print(f'Area of two point({p1}, {p2}) is {res}')

if __name__ == "__main__":
    main()
